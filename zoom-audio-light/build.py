"""index.html + img/ 를 이미지 내장 단일 파일로 묶는다.

출력:
  zoom-audio-light.html           : claude.ai 페이지 링크용 (index.html과 같은 골격, 이미지만 내장)
  zoom-audio-light-preview.html   : 브라우저에서 바로 여는 미리보기 (doctype 포함)
"""
import base64, io, re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
s = (ROOT / "index.html").read_text(encoding="utf-8")
cache = {}

def embed(m):
    f = m.group(1)
    if f not in cache:
        im = Image.open((ROOT / f).resolve()).convert("RGBA")
        lim = 1600 if "/scenes/" in f else 700
        if max(im.size) > lim:
            k = lim / max(im.size)
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=82, method=6)
        cache[f] = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
    return 'src="' + cache[f] + '"'

out = re.sub(r'src="((?:\.\./)?[^"]*img/[^"]+)"', embed, s)
(ROOT / "zoom-audio-light.html").write_text(out, encoding="utf-8")
(ROOT / "zoom-audio-light-preview.html").write_text(
    '<!doctype html>\n<html lang="ko"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>\n'
    + out + "\n</body></html>\n", encoding="utf-8")
print(f"zoom-audio-light.html {len(out)//1024}KB, images {len(cache)}")
