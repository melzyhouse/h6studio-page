"""4안 index.html 생성기.

- 제품·카테고리 데이터는 아래 CATEGORIES 에서 관리 (가격·링크: AVX 자사몰 ZOOM 브랜드관, 2026-11)
- 각 제품은 본문에 한 번만 나온다. 박스 크기(size)는 제품의 무게에 따라 다르게.
  size: big(가로 8칸·세로 2줄) / tall(4칸·2줄) / wide(6~7칸) / small(3~4칸)
- 상단 제품군 아이콘 줄과 슬라이드는 3안(zoom-audio-light)에서 가져온 것
실행: python3 make_page.py && python3 build.py
"""
from pathlib import Path
import html, json

ROOT = Path(__file__).parent
e = html.escape
AVX = "https://www.avx.co.kr/goods/view?no={}"

CATEGORIES = [
    dict(id="handy", rep="h6studio", rep_size="rep2 c6", label="HANDY RECORDER", title="핸디 레코더", intro="손에 쥐고 바로 녹음. 합주실, 무대, 책상 위까지.", icon="h6studio", items=[
        dict(k="h6studio", n="H6studio", size="big c8 r2", tag="NEW", sub="여섯 트랙. 대구경 XY 마이크.", specs=["6 + 2 MIX", "32-BIT FLOAT", "XLR/TRS ×4", "AA · 15H"], price="699,000원", no=2545, more="https://claude.ai/artifact/SCHGy9TERkg3ViwjEJdivj"),
        dict(k="h5studio", n="H5studio", size="tall c4 r2", sub="4트랙 스튜디오 핸디 레코더. 오디오 인터페이스로도.", price="659,000원", no=2277),
        dict(k="h6e", n="H6essential", size="small c3", tag="FIRMWARE V4.0", sub="6트랙 32비트 플로트. 이제 멀티트랙 녹음 모드까지.", price="559,000원", no=1465),
        dict(k="h4e", n="H4essential", size="small c3", sub="4트랙 32비트 플로트.", price="399,000원", no=1468),
        dict(k="h2e", n="H2essential", size="small c3", sub="32비트 플로트 핸디 레코더.", price="339,000원", no=1919),
        dict(k="h1e", n="H1essential", size="small c3 white", tag="START HERE", sub="처음 사는 녹음기라면. 가볍게 시작하는 32비트.", price="199,000원", no=1469),
    ]),
    dict(id="field", rep="f3", rep_size="rep2 c6", label="FIELD RECORDER", title="필드 레코더", intro="촬영장과 야외에서. 갑자기 커지는 소리에도 깨지지 않게.", icon="f6", items=[
        dict(k="f8npro", n="F8n Pro", size="tall c5 r2 dark", sub="8채널 필드 레코더.", price="1,700,000원", no=423),
        dict(k="f6", n="F6", size="wide c7", sub="멀티트랙 필드 레코더. 전용 가방 PCF-6 포함.", price="1,030,000원", no=534),
        dict(k="f3", n="F3", size="wide c7", sub="2채널 32비트 플로트 필드 레코더.", price="530,000원", no=922),
    ]),
    dict(id="effects", rep="neurig", rep_size="rep2 c6", label="MULTI-EFFECTS", title="이펙터", intro="페달 하나로 시작해 보드 전체까지. 합주실에 들고 가는 톤.", icon="g1four", items=[
        dict(k="neurig", n="NEURIG", size="tall c6 r2 dark", tag="COMING SOON", sub="기타 앰프와 이펙트를, 뉴럴 모델링으로.", price="가격 문의 · 국내 안전 인증 진행 중", no=3201, cta="출시 문의"),
        dict(k="g1four", n="G2 FOUR / G2X FOUR", size="wide c6", sub="기타 멀티 이펙트 프로세서.", price="357,000원", no=3024),
        dict(k="b2four", n="B2 FOUR", size="small c3", sub="베이스 멀티 이펙트 프로세서.", price="446,000원", no=3023),
        dict(k="ms70cdr", n="MS-70CDR+", size="small c3", sub="코러스·딜레이·리버브 멀티스톰프.", price="214,000원", no=2989),
    ]),
    dict(id="vocal", rep="v6sp", rep_size="rep2 c6", label="VOCAL PROCESSOR", title="보컬", intro="하모니, 피치, 루프. 목소리 하나로 무대를 채우는 이펙터.", icon="v6sp", items=[
        dict(k="v6sp", n="V6-SP", size="wide c7", sub="보컬 이펙터·루퍼·포먼트를 발끝으로.", price="660,000원", no=2995),
        dict(k="v3", n="V3", size="wide c5", sub="하모니·피치 코렉트 보컬 프로세서. USB 오디오 인터페이스.", price="499,000원", no=2994),
    ]),
    dict(id="mixer", rep="l12next", rep_size="rep2 c6", label="MIXER · RECORDER", title="믹서·레코더", intro="합주를 섞고, 그대로 기록하는 장비.", icon="l6max", items=[
        dict(k="l12next", n="LiveTrak L12next", size="wide c8", sub="12채널 14트랙 디지털 믹서·레코더.", price="1,150,000원", no=2738),
        dict(k="l6max", n="LiveTrak L6max", size="small c4", sub="12채널 포터블 오디오 레코더.", price="570,000원", no=2684),
        dict(k="r20", n="R20 MultiTrak", size="wide c12", sub="멀티트랙 레코더.", price="891,000원", no=2977),
    ]),
    dict(id="podcast", rep="p4next", rep_size="rep2 c6", label="PODCAST", title="팟캐스트", intro="둘이서, 넷이서. 마이크를 꽂고 버튼 몇 번이면 대화가 깨끗하게.", icon="p4next", items=[
        dict(k="p4next", n="PodTrak P4next", size="wide c8", sub="4트랙 팟캐스트 레코더. 오디오 인터페이스로도.", price="305,000원", no=2680),
        dict(k="p2", n="PodTrak P2", size="small c4", sub="2트랙 팟캐스트 레코더.", price="199,000원", no=2282),
    ]),
]


def rep_tile(c):
    it = next(x for x in c["items"] if x["k"] == c["rep"])
    size = c["rep_size"] + " " + ("tone-1", "tone-2", "tone-3")[CATEGORIES.index(c) // 2]
    tag = ""
    specs = ""
    head = "h3"
    return f'''      <a class="tile p-tile rep {size} rise" href="#{c["id"]}" data-series="{c["id"]}" aria-label="{e(c["title"])} 시리즈 보기, 대표 제품 {e(it["n"])}">
        <div class="p-copy">{tag}<span class="cat-name">{e(c["title"])}</span><{head}>{e(it["n"])}</{head}><p>{e(it["sub"])}</p>{specs}<p class="price{"" if it["price"][0].isdigit() else " kr"}">{e(it["price"])}</p><span class="see">시리즈 보기 ›</span><span class="count">{len(c["items"])}개 제품</span></div>
        <img class="art" data-src="{it["k"]}" alt="">
      </a>'''


src = (ROOT / "template.html").read_text(encoding="utf-8")
chapter = "\n".join(f'    <a href="#{c["id"]}" data-series="{c["id"]}"><span>{e(c["title"])}</span></a>' for c in CATEGORIES)
keys = [it["k"] for c in CATEGORIES for it in c["items"]]
imgs = "\n".join(f'  <img data-k="{k}" src="../zoom-studio-home/img/products/{k}.png" alt="">' for k in dict.fromkeys(keys))
cats = [dict(id=c["id"], label=c["label"], title=c["title"], intro=c["intro"],
             items=[dict(k=it["k"], n=it["n"], sub=it["sub"], price=it["price"], no=it["no"], tag=it.get("tag", ""), more=it.get("more", "")) for it in c["items"]])
        for c in CATEGORIES]
out = (src.replace("<!--CHAPTER-->", chapter)
          .replace("<!--REPS-->", "\n".join(rep_tile(c) for c in CATEGORIES))
          .replace("<!--IMGSRC-->", imgs)
          .replace("/*CATS*/[]", json.dumps(cats, ensure_ascii=False)))
(ROOT / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out) // 1024, "KB,", len(CATEGORIES), "categories,", len(keys), "products")
