"""slots_data.py 로부터 이미지 작업표 페이지(worklist.html)를 만든다."""
import base64, html, io, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from slots_data import SLOTS, LEVEL_LABEL

def thumb(fname):
    p = ROOT / "img" / "slots" / fname
    if not fname or not p.exists():
        return None
    im = Image.open(p).convert("RGBA")
    im.thumbnail((360, 270))
    bg = Image.new("RGBA", im.size, (128, 128, 128, 255))   # 투명 영역이 보이도록 회색 바탕
    bg.alpha_composite(im)
    buf = io.BytesIO(); bg.convert("RGB").save(buf, "WEBP", quality=78)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()

order = {"bad": 0, "warn": 1, "fixed": 2, "ok": 3}
counts = {k: sum(1 for s in SLOTS if s[3] == k) for k in order}
e = html.escape

cards = []
for sid, sec, fname, lv, lab, prob, need in SLOTS:
    t = thumb(fname)
    if t:
        media = f'<img src="{t}" alt="{e(sid)} 현재 이미지" loading="lazy">'
    else:
        media = f'<div class="noimg">{"그래픽으로 대체" if fname.startswith("(") else "이미지 없음"}</div>'
    file_line = f'<code>img/slots/{e(fname)}</code>' if fname and not fname.startswith("(") else '<span class="muted">파일 없음 · 새로 추가</span>'
    cards.append(f'''
    <article class="slot" data-level="{lv}">
      <div class="thumb">{media}</div>
      <div class="body">
        <header><span class="sid">{sid}</span><span class="pill {lv}">{LEVEL_LABEL[lv]}</span><span class="sec">{e(sec)}</span></header>
        <dl>
          <dt>현재 상태</dt><dd>{e(prob)}</dd>
          <dt>필요한 이미지</dt><dd>{e(need)}</dd>
          <dt>바꿀 파일</dt><dd>{file_line}</dd>
        </dl>
      </div>
    </article>''')

page = f'''<title>H6studio 이미지 작업표</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* 작업 목록: 상단 요약 + 필터, 아래로 슬롯 카드 목록 */
:root {{
  --bg: #f5f5f7; --surface: #ffffff; --fg: #1d1d1f; --muted: #6e6e73; --line: #d2d2d7;
  --bad: #d70015; --bad-bg: #ffe9e7; --warn: #b25000; --warn-bg: #fff2e0;
  --fixed: #0060b8; --fixed-bg: #e5f1ff; --ok: #0a7a1a; --ok-bg: #e3f6e7; --accent: #0071e3;
  --font: "Pretendard", "Apple SD Gothic Neo", "SF Pro KR", "Noto Sans KR", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #111113; --surface: #1d1d1f; --fg: #f5f5f7; --muted: #98989d; --line: #3a3a3c;
  --bad: #ff6961; --bad-bg: #3a1614; --warn: #ffb340; --warn-bg: #3a2810;
  --fixed: #64b5ff; --fixed-bg: #10253d; --ok: #4cd964; --ok-bg: #13301a; --accent: #2997ff; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #111113; --surface: #1d1d1f; --fg: #f5f5f7; --muted: #98989d; --line: #3a3a3c;
  --bad: #ff6961; --bad-bg: #3a1614; --warn: #ffb340; --warn-bg: #3a2810;
  --fixed: #64b5ff; --fixed-bg: #10253d; --ok: #4cd964; --ok-bg: #13301a; --accent: #2997ff; color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--fg); font: 15px/1.55 var(--font); word-break: keep-all; letter-spacing: -0.01em; }}
.wrap {{ max-width: 1040px; margin: 0 auto; padding-block: 48px 72px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1 {{ font-size: clamp(28px, 5vw, 40px); line-height: 1.15; margin: 0 0 8px; letter-spacing: -0.02em; text-wrap: balance; }}
.lead {{ color: var(--muted); max-width: 64ch; margin: 0 0 28px; }}
.summary {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 28px; }}
.summary button {{ border: 1px solid var(--line); background: var(--surface); color: var(--fg); border-radius: 999px; padding: 8px 14px; font: 600 14px/1 var(--font); cursor: pointer; display: inline-flex; gap: 8px; align-items: center; }}
.summary button[aria-pressed="true"] {{ border-color: var(--fg); box-shadow: inset 0 0 0 1px var(--fg); }}
.summary button:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
.summary b {{ font-variant-numeric: tabular-nums; }}
.dot {{ width: 8px; height: 8px; border-radius: 50%; }}
.how {{ background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 20px 24px; margin-bottom: 32px; }}
.how h2 {{ font-size: 17px; margin: 0 0 10px; }}
.how ol {{ margin: 0; padding-left: 20px; display: grid; gap: 6px; }}
code {{ font: 13px/1.4 ui-monospace, "SF Mono", Menlo, monospace; background: var(--bg); padding: 2px 6px; border-radius: 6px; word-break: break-all; }}
.list {{ display: grid; gap: 16px; }}
.slot {{ display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 20px; background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 16px; }}
.slot[hidden] {{ display: none !important; }}
.thumb {{ border-radius: 10px; overflow: hidden; background: #808080; aspect-ratio: 4/3; display: grid; place-items: center; max-width: 100%; }}
.thumb img {{ width: 100%; height: 100%; object-fit: contain; display: block; }}
.noimg {{ color: #fff; font-weight: 600; font-size: 14px; }}
.body header {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px 10px; margin-bottom: 10px; }}
.sid {{ font: 700 15px/1 ui-monospace, "SF Mono", Menlo, monospace; }}
.sec {{ font-weight: 600; }}
.pill {{ font: 600 12px/1 var(--font); padding: 5px 9px; border-radius: 999px; }}
.pill.bad {{ color: var(--bad); background: var(--bad-bg); }} .pill.warn {{ color: var(--warn); background: var(--warn-bg); }}
.pill.fixed {{ color: var(--fixed); background: var(--fixed-bg); }} .pill.ok {{ color: var(--ok); background: var(--ok-bg); }}
dl {{ margin: 0; display: grid; grid-template-columns: 96px minmax(0, 1fr); gap: 6px 12px; }}
dt {{ color: var(--muted); font-size: 13px; padding-top: 1px; }}
dd {{ margin: 0; }}
.muted {{ color: var(--muted); }}
@media (max-width: 640px) {{
  .slot {{ grid-template-columns: 1fr; }}
  dl {{ grid-template-columns: 1fr; gap: 2px; }} dd {{ margin-bottom: 8px; }}
}}
</style>
<div class="wrap">
  <h1>H6studio 이미지 작업표</h1>
  <p class="lead">상세페이지 시안에 들어간 이미지 {len(SLOTS)}개 슬롯의 상태입니다. 원본 사이트 이미지의 해상도·비율·내용 한계 때문에 타협한 곳과, 제가 손으로 보정한 곳을 구분했습니다. 시안 페이지 주소 끝에 <code>#slots</code>를 붙이면 같은 번호가 이미지 위에 표시됩니다.</p>
  <div class="summary" role="group" aria-label="상태별 보기">
    <button type="button" data-f="all" aria-pressed="true">전체 <b>{len(SLOTS)}</b></button>
    <button type="button" data-f="bad" aria-pressed="false"><span class="dot" style="background:var(--bad)"></span>꼭 필요 <b>{counts["bad"]}</b></button>
    <button type="button" data-f="warn" aria-pressed="false"><span class="dot" style="background:var(--warn)"></span>권장 <b>{counts["warn"]}</b></button>
    <button type="button" data-f="fixed" aria-pressed="false"><span class="dot" style="background:var(--fixed)"></span>보정함 <b>{counts["fixed"]}</b></button>
    <button type="button" data-f="ok" aria-pressed="false"><span class="dot" style="background:var(--ok)"></span>그대로 <b>{counts["ok"]}</b></button>
  </div>
  <section class="how">
    <h2>이미지 바꾸는 법</h2>
    <ol>
      <li>새 이미지를 아래 "바꿀 파일"과 <b>같은 이름</b>으로 <code>h6studio-page/img/slots/</code>에 넣습니다. 누끼는 PNG(투명 배경)로 저장합니다.</li>
      <li>이미지가 없는 슬롯(S09, S10)은 파일을 넣어 주시면 제가 카드에 연결합니다.</li>
      <li><code>python3 build.py</code>를 실행하면 페이지에 반영됩니다. <code>make_slots.py</code>는 다시 돌리지 마세요. 넣은 파일이 원래대로 덮어써집니다(<code>--keep</code>을 붙이면 안전).</li>
    </ol>
  </section>
  <div class="list">{"".join(sorted(cards, key=lambda c: order[c.split('data-level="')[1].split('"')[0]]))}
  </div>
</div>
<script>
  const btns = document.querySelectorAll('.summary button');
  btns.forEach(b => b.addEventListener('click', () => {{
    btns.forEach(x => x.setAttribute('aria-pressed', x === b));
    document.querySelectorAll('.slot').forEach(s => {{ s.hidden = b.dataset.f !== 'all' && s.dataset.level !== b.dataset.f; }});
  }}));
</script>
'''
(ROOT / "worklist.html").write_text(page, encoding="utf-8")
print("worklist.html", len(page) // 1024, "KB", counts)
