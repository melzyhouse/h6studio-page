# H6studio 상세페이지 프로젝트

ZOOM H6studio 핸디 레코더 상세페이지를 Apple MacBook Neo 페이지 스타일로 만든 디자인 시안.
사용자는 한국어로 대화한다. 답변도 한국어로.

## 폴더
- `zoom-audio-bento/` : **ZOOM AUDIO 홈페이지 4안 (현재 진행안)** — 3안 상단(제품군 아이콘 줄 + 제품 슬라이드) 유지 + 본문은 ZOOM 카테고리별 벤토 그리드(핸디 레코더 / 필드 레코더 / 이펙터 / 보컬 / 믹서·레코더 / 팟캐스트). 제품 카드는 본문에 한 번씩만. 박스 크기는 제품 무게·모양에 따라(big/tall/wide/small). 그 아래 용도별로 찾기 도구 박스, 정품·A/S
  - **수정 순서:** 제품·카테고리·박스 크기는 `make_page.py`의 `CATEGORIES` → 레이아웃·스타일·스크립트는 `template.html` → `python3 make_page.py && python3 build.py`. `index.html`은 생성물이라 직접 고치지 말 것
  - 사용자 피드백: Apple처럼 깔끔·둥근 박스·밝은 톤 선호, 네이비 싫음(어두운 곳은 회색 차콜), 박스가 규칙적으로 반복되는 배열은 싫음, 사진 대신 제품으로 정리, 제품 중복 노출 싫음, 타이틀 굵기 700
  - 게시 링크: https://claude.ai/artifact/G3aF9EpYdTGGzjzsSeoiG9
- `zoom-audio-light/` : **ZOOM AUDIO 홈페이지 3안 (Apple 톤, 4안의 바탕)** — 2안 구성 그대로, 흰색 #FFFFFF·연회색 #F5F5F7 바탕 + 검정 글자 + ZOOM 블루 #2362FF 포인트. 네이비는 쓰지 않음. 어두운 구간(신제품 패널, 출시 예정)은 회색 차콜 #2A2B2F, 그 안에서만 라임 포인트
  - 상단: 제품군 아이콘 줄(`.chapter`) + 제품 히어로 슬라이드 3장(`.stage`: H6studio / F 시리즈 / LiveTrak L6max, 6초 자동 넘김). 큰 문장+사진 히어로는 '홈페이지 같지 않다'는 피드백으로 제거
  - 용도별로 찾기: 1안처럼 제품 카드 가로 갤러리(연회색 카드, 자동 넘김+점). 데이터는 스크립트의 `USES` 배열. 사진형 채널 스트립은 피드백으로 제거
  - 2안 index.html을 복사해 `<style>` 끝에 라이트·차콜 덮어쓰기 CSS를 붙인 구조. 이미지는 ../zoom-audio-home, ../zoom-studio-home 공유
  - `python3 build.py` → `zoom-audio-light.html`(게시용)
  - 게시 링크: https://claude.ai/artifact/WUzJV9XzhrBfjd4oZ3chSu
- `zoom-audio-home/` : **ZOOM AUDIO 홈페이지 2안 (네이비 버전, 비교용)** — Apple 홈 구조에서 벗어나 장비·뮤지션 톤으로 재구성
  - 히어로(연주 사진+왼쪽 정렬 타이포) → 신제품 H6studio(장비 화면 패널) → 채널 스트립 '어디서 연주하나요?'(CH 01~06, 레벨 미터) → 전체 라인업(필터 탭, 20종) → 출시 예정 NEURIG → 신호 흐름 정품·A/S + FAQ → 푸터
  - 제품 데이터(이름·설명·가격·AVX 상품번호)는 index.html 스크립트의 `PRODUCTS` 배열, 용도별 구성은 `CH` 배열에서 수정
  - 제품 이미지는 `../zoom-studio-home/img/products/` 공유, 사용 장면 사진은 `img/scenes/` (아티스트 실명 사진은 홍보 오해 소지가 있어 제외)
  - `python3 build.py` → `zoom-audio.html`(게시용) / `zoom-audio-preview.html`
  - 게시 링크: https://claude.ai/artifact/WgDHUfEdeuXHwKHgJUD3PK
- `zoom-studio-home/` 은 1안(Apple 홈 구성 그대로, 비교용으로 보관). 링크 https://claude.ai/artifact/3RPxPbxKGWfGUaGpFeWBak
- `zoom-studio-home/` : **ZOOM AUDIO 홈페이지 시안 (폴더명은 zoom-studio-home 그대로)** (apple.com/kr 홈페이지 구성)
  - `index.html` 원본 → `python3 build.py` → `zoom-studio.html`(게시용, 이미지 내장) / `zoom-studio-preview.html`(로컬 미리보기)
  - `img/products/` : zoomcorp.com 공식 목록용 투명 PNG(정면 컷, 1000px로 정리)
  - 게시 링크: https://claude.ai/artifact/3RPxPbxKGWfGUaGpFeWBak
  - 브랜드 기준: 노션 'AVX ZOOM 인스타 디자인 지침 (2026-11-16 최신)' — 차콜 네이비 #1B2545, 하단 블루 그라데이션 #1D3B8E→#204DC1→#215AE6(불투명도 0.7), 라임 #C8FF4D는 라벨·LED 등 찾아 읽는 정보에만
  - 가격·링크는 AVX 자사몰 ZOOM 브랜드관(https://www.avx.co.kr/goods/brand?code=0004) 기준
- `macbook-neo-study/` : apple.com/kr/macbook-neo 페이지를 코드로 분석한 학습 자료
  - `README.md` 구조·카피 톤·디자인 원칙, `design-tokens.css` 색·폰트·간격 토큰, `raw/` 원본 HTML/CSS
- `h6studio-page/` : 상세페이지 시안
  - `index.html` : **원본. 수정은 여기서.**
  - `design-tokens.css` : 위 학습 자료의 토큰
  - `img/` : zoomcorp.com 원본 이미지, `img/orig/` 고해상도 원본, `img/adobe/` Adobe 배경 제거 결과
  - `img/slots/` : 페이지에 실제 들어가는 슬롯별 이미지 (S01~S35)
  - `slots_data.py` : 슬롯 목록·상태(bad/warn/fixed/ok)·필요한 이미지 규격
  - `make_slots.py` : img/ 원본 → img/slots/ 생성(크롭·누끼 보정 포함). **`--keep` 없이 다시 돌리면 직접 바꿔 넣은 슬롯 파일이 덮어써진다.**
  - `build.py` : index.html + 이미지를 단일 파일로 묶음 → `h6studio-preview.html`(미리보기), `h6studio-artifact.html`(claude.ai 페이지 링크용)
  - `make_worklist.py` : slots_data.py → `worklist.html`(이미지 작업표)

## 작업 순서
1. `index.html` 수정 (또는 `img/slots/`의 파일을 같은 이름으로 교체)
2. `cd h6studio-page && python3 build.py` (슬롯 상태를 바꿨으면 `python3 make_worklist.py`도)
3. 브라우저로 데스크톱·모바일(390px) 확인
4. 게시된 페이지 업데이트: Artifact 도구로 `h6studio-artifact.html`을 아래 URL에 publish
   - 상세페이지: https://claude.ai/artifact/SCHGy9TERkg3ViwjEJdivj
   - 이미지 작업표: https://claude.ai/artifact/359CuS8f5PtuZeNZDoqzLY (`worklist.html`)

## 지켜야 할 것
- 공식 ZOOM 페이지로 오해되지 않도록 게시본 상단 띠의 "디자인 스타일 학습용 시안" 문구 유지 (build.py가 넣음)
- 가격은 국내 정식 판매처 에이브이엑스(AVX) 기준: H6studio 699,000원 / H5studio 659,000원 / H6essential 559,000원 (2026년 11월 확인). 구입 버튼 → https://www.avx.co.kr/goods/view?no=2545
- 라이트(기본)/다크 테마 토글, 스크롤 모션, 32비트 플로트 파형 데모, `#slots` 디버그 모드가 있음. 한쪽 테마만 고치지 말 것
- 이미지 출처는 zoomcorp.com (ZOOM 저작물). 시안 용도

## 남은 일 (slots_data.py의 bad/warn)
- 꼭 필요: S02·S03 하이라이트 카드용 세로 사진(744×1200+), S09 포맷 스위치 클로즈업
- 추천: 비교 카드 S32~34 같은 정면 각도 누끼(Adobe 배경 제거 사용), 히어로 S01 고해상도 누끼
- Adobe 도구 사용 시: zoomcorp.com URL은 직접 못 받음 → 파일을 받아 asset_initialize_file_upload로 올린 뒤 처리
