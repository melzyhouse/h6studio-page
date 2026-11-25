"""index.html + img/ + design-tokens.css 를 단일 파일로 묶는다.

출력:
  h6studio-preview.html  : 채팅 미리보기/브라우저용 (이미지 내장)
  h6studio-artifact.html : claude.ai 페이지 링크용 (스켈레톤 태그 제거, 시안 표기)
"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
s = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "design-tokens.css").read_text(encoding="utf-8")
s = s.replace('<link rel="stylesheet" href="design-tokens.css">', "<style>\n" + css + "\n</style>")

# 슬롯 상태를 페이지에 주입 (#slots 모드 배지용)
import json
sys.path.insert(0, str(ROOT))
from slots_data import SLOTS, LEVEL_LABEL
state = {sid: {"level": lv, "label": LEVEL_LABEL[lv] + (" · " + lab if lab else "")} for sid, _, _, lv, lab, _, _ in SLOTS}
s = s.replace("<script>\n(() => {", "<script>window.SLOT_STATE = " + json.dumps(state, ensure_ascii=False) + ";</script>\n<script>\n(() => {", 1)

cache = {}
def embed(m):
    f = m.group(1)
    if f not in cache:
        im = Image.open(ROOT / "img" / f)
        if im.width > 1400:
            im = im.resize((1400, round(im.height * 1400 / im.width)))
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=80)
        cache[f] = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
    return 'src="' + cache[f] + '"'
s = re.sub(r'src="img/([^"]+)"', embed, s)
(ROOT / "h6studio-preview.html").write_text(s, encoding="utf-8")

a = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", s, flags=re.I)
a = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*', "", a)
a = re.sub(r"</head>\s*<body>", "", a)
a = re.sub(r"</body>\s*</html>\s*$", "", a)
for old, new in [
    ("<title>H6studio - ZOOM</title>", "<title>H6studio 디자인 시안</title>"),
    (".localnav { position: sticky; top: 0;", ".localnav { position: sticky; top: env(safe-area-inset-top, 0px);"),
    ("html { overflow-x: clip; scroll-behavior: smooth; }",
     "html { overflow-x: clip; scroll-behavior: smooth; color-scheme: light; }\n"
     '  body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 30; background: var(--band, #161617); }'),
    (".reveal { opacity: 0; transform: translateY(40px);", ".reveal { opacity: 1; transform: translateY(28px);"),
    ('<div class="ribbon">H6studio 액세서리 팩 APH-6st와 함께 더 완벽하게. <a class="link-arrow" href="#">더 알아보기</a></div>',
     '<div class="ribbon">디자인 스타일 학습용 시안이며 ZOOM 공식 페이지가 아닙니다. '
     '<a class="link-arrow" href="https://zoomcorp.com/en/us/handheld-recorders/handheld-recorders/h6studio/">공식 페이지 보기</a></div>'),
]:
    if old not in a:
        sys.exit("build: pattern not found: " + old[:60])
    a = a.replace(old, new)
(ROOT / "h6studio-artifact.html").write_text(a, encoding="utf-8")
print(f"preview {len(s)//1024}KB, artifact {len(a)//1024}KB")
