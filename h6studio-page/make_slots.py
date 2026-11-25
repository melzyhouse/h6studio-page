"""img/ 원본에서 슬롯별 이미지(img/slots/)를 만든다. 손작업 보정도 여기서 한다.

슬롯 파일을 직접 만든 이미지로 바꾸고 싶으면:
  1) img/slots/ 의 해당 파일을 같은 이름으로 덮어쓰고
  2) 이 스크립트 대신 build.py 만 실행한다. (이 스크립트를 다시 돌리면 덮어쓴 파일이 원래대로 돌아감)
  --keep 옵션을 주면 이미 있는 슬롯 파일은 건드리지 않는다.
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC = Path(__file__).parent / "img"
OUT = SRC / "slots"
OUT.mkdir(exist_ok=True)
KEEP = "--keep" in sys.argv


def save(im, name):
    p = OUT / name
    if KEEP and p.exists():
        return
    if p.suffix == ".jpg":
        im.convert("RGB").save(p, quality=90)
    else:
        im.save(p)


def white_cutout(path, thresh=218):
    """흰 배경 제품컷 → 투명 PNG.
    가장자리와 이어진 밝은 영역만 배경으로 보고(flood fill), 그 영역은 color-to-alpha로
    처리해 그림자는 반투명 검정으로 남긴다. 제품 안쪽의 밝은 부분(마이크 메시 등)은 그대로."""
    im = Image.open(SRC / path).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    lum = a.min(axis=2)
    bright = Image.fromarray(((lum > thresh) * 255).astype(np.uint8)).copy()  # copy: fromarray 뷰는 floodfill이 안 먹음
    w, h = bright.size
    for x, y in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]:
        if bright.getpixel((x, y)) == 255:
            ImageDraw.floodfill(bright, (x, y), 128)
    bg = (np.asarray(bright) == 128)
    # 배경 영역을 살짝 넓혀 경계의 밝은 테두리 제거
    bg_img = Image.fromarray((bg * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))
    bg = np.asarray(bg_img) > 0
    # 그림자 영역(배경과 이어진 약간 어두운 부분)까지 color-to-alpha
    soft = Image.fromarray((bg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
    soft = np.asarray(soft).astype(np.float32) / 255
    alpha_c2a = np.clip((255 - a).max(axis=2) / 255 * 1.15, 0, 1)
    alpha = alpha_c2a * soft + 1.0 * (1 - soft)
    alpha = np.where(bg & (lum > 245), 0, alpha)
    # 색 복원: c = a*fg + (1-a)*255
    fg = np.where(alpha[..., None] > 0.01, (a - (1 - alpha[..., None]) * 255) / np.maximum(alpha[..., None], 0.01), 0)
    rgba = np.dstack([np.clip(fg, 0, 255), alpha * 255]).astype(np.uint8)
    out = Image.fromarray(rgba, "RGBA")
    return out.crop(out.getbbox())


def trim_to_height(path, height):
    im = Image.open(SRC / path).convert("RGBA")
    im = im.crop(im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
    return im.resize((round(im.width * height / im.height), height), Image.LANCZOS)


def adobe(name_in, out, pad=0):
    """Adobe Photoshop API(배경 제거)로 만든 누끼(img/adobe/)를 투명 여백만 잘라 사용."""
    im = Image.open(SRC / "adobe" / name_in).convert("RGBA")
    im = im.crop(im.getchannel("A").point(lambda v: 255 if v > 6 else 0).getbbox())
    save(im, out)


def copy(path, name):
    save(Image.open(SRC / path), name)


# ── 히어로 ──
copy("hero.png", "S01-hero.png")
# ── 하이라이트 카드 ──
copy("clip.jpg", "S02-hl-float.jpg")
copy("studio.jpg", "S03-hl-tracks.jpg")
adobe("mics.png", "S04-hl-mics.png")                          # Adobe 배경 제거
copy("podcast.jpg", "S05-hl-podcast.jpg")
copy("sampling.jpg", "S06-hl-sampling.jpg")
adobe("battery.png", "S07-hl-battery.png")                    # Adobe 배경 제거
# ── 32비트 ──
copy("gain.jpg", "S08-float-wide.jpg")
# ── 사운드 ──
adobe("mics.png", "S11-sound-xy.png")                        # Adobe 배경 제거
adobe("preamps.png", "S12-sound-preamp.png")                 # Adobe 배경 제거
# ── 입출력 ──
copy("inputs.jpg", "S13-io-inputs.jpg")
copy("outputs.png", "S14-io-outputs.png")
# ── 캡슐 ──
copy("cap-xy.jpg", "S15-cap-xy.jpg")
copy("cap-ssh.jpg", "S16-cap-ssh.jpg")
copy("cap-exh.jpg", "S17-cap-exh.jpg")
# ── 프로 기능 ──
copy("rf.jpg", "S19-pro-rf.jpg")
tc = Image.open(SRC / "tc.jpg")                                # 손작업: 화면 부분만 크롭
save(tc.crop((60, 0, 420, 300)), "S20-pro-display.jpg")
# ── 싱크 ──
copy("tc.jpg", "S21-sync-tc.jpg")
copy("app.jpg", "S23-sync-app.jpg")
# ── USB ──
copy("usb.jpg", "S24-usb-wide.jpg")
# ── 전원/저장 ──
adobe("battery.png", "S25-spec-battery.png")                  # Adobe 배경 제거
copy("sd.jpg", "S26-spec-sd.jpg")
acc = Image.open(SRC / "access.png")                           # 손작업: 위쪽 잘린 파란 선 제거
save(acc.crop((0, 14, acc.width, acc.height)), "S27-spec-access.png")
# ── 갤러리 (p2는 p3와 거의 같은 컷이라 제외) ──
copy("p3.jpg", "S28-gal-front.jpg")
copy("p4.jpg", "S29-gal-back.jpg")
copy("p7.jpg", "S30-gal-detail.jpg")
# ── 비교: 투명 여백을 잘라 같은 높이로 맞춤 ──
for src, name in [("h5.png", "S32-cmp-h5.png"), ("hero.png", "S33-cmp-h6studio.png"), ("h6e.png", "S34-cmp-h6e.png")]:
    save(trim_to_height(src, 520), name)
# ── 아웃트로: 영문 카피가 박힌 아래쪽을 잘라냄 ──
o = Image.open(SRC / "outro.jpg")
save(o.crop((0, 0, o.width, round(o.height * 0.6))), "S35-outro.jpg")
print("slots:", len(list(OUT.iterdir())))
