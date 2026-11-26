# ZOOM AUDIO 홈페이지 · H6studio 상세페이지 작업 정리

작업 기간: 2026-11-25 ~ 11-26 (Claude Code 클라우드 세션)
원본 저장소: https://github.com/melzyhouse/h6studio-page (비공개) — 폴더 구조·수정 방법·전체 기준은 저장소의 `CLAUDE.md`

## 결과물 링크
| 페이지 | 상태 | 링크 |
|---|---|---|
| ZOOM AUDIO 홈페이지 4안 | **현재 진행안** | https://claude.ai/artifact/G3aF9EpYdTGGzjzsSeoiG9 |
| 3안 (밝은 Apple 톤) | 보관 | https://claude.ai/artifact/WUzJV9XzhrBfjd4oZ3chSu |
| 2안 (네이비, 장비 톤) | 보관 | https://claude.ai/artifact/WgDHUfEdeuXHwKHgJUD3PK |
| 1안 (Apple 홈 구조 그대로) | 보관 | https://claude.ai/artifact/3RPxPbxKGWfGUaGpFeWBak |
| H6studio 상세페이지 (MacBook Neo 스타일) | 완료 | https://claude.ai/artifact/SCHGy9TERkg3ViwjEJdivj |
| H6studio 이미지 작업표 | 참고 | https://claude.ai/artifact/359CuS8f5PtuZeNZDoqzLY |

## 홈페이지 4안 구성
1. 상단 내비: ZOOM / AUDIO 워드마크 · 제품 · 용도별 추천 · 고객 지원 · "한국 공식 수입원 AVX" · 구매하기 · **매뉴얼·펌웨어(맨 오른쪽)**
2. 제품군 줄(텍스트만): 핸디 레코더 · 필드 레코더 · 이펙터 · 보컬 · 믹서·레코더 · 팟캐스트 → 누르면 시리즈 시트
3. 메인 배너 슬라이드 3장: H6studio / F 시리즈 / LiveTrak L6max
4. 카테고리 배너 2열×3줄 (카테고리별 최신 대표 제품 1개): H6studio · F3 · NEURIG · V6-SP · LiveTrak L12next · PodTrak P4next → 누르면 그 카테고리 전체 제품 시트 → 자세히 보기(상세)
5. 용도별 추천: 합주·공연 / 홈레코딩 / 사운드 메이킹 / 보컬 / 팟캐스트·방송 / 영상·현장. 가로 폭 안에 3개씩 보이고 순환. 제품명에 마우스를 올리면 이미지 변경
6. 고객 지원: 자료실 / 기술 상담 / A/S 탭 → 누르면 아래에 내용
7. 푸터: 제품 링크, 가격 기준 각주, 에이브이엑스(주) 정보

## 디자인 기준 (사용자 피드백으로 확정)
- **Apple 톤**: 깔끔한 정리, 흰색·회색 바탕, 가운데 정렬 배너. apple.com/kr 실측 수치 사용
  - 메인 배너 높이 692(데스크톱·화면 높이 776 이상) / 580 / 650·570(태블릿) / 500(모바일)
  - 카테고리 배너는 화면 끝까지 2열, 배너 사이 12px, 바탕 #F5F5F7 공유, 높이 580 / 490 / 500(모바일 1열)
- **네이비 쓰지 않음.** 차콜 덩어리로 강조하지 않고 회색 톤 단계로 명암: #FFFFFF / #F5F5F7 / #EEEFF2 / #E6E7EB / #DCDDE2
- 포인트 색은 ZOOM 블루 #2362FF 하나
- 둥근 버튼(알약형), 타이틀 굵기 700
- 제목 위 파란 점·영문 라벨 쓰지 않음
- 제품 이미지는 모양이 달라도 **보이는 면적이 같게** 크기 계산(대표 배너·용도별 카드 모두)
- 같은 제품을 본문에 중복 배치하지 않음 (대표 제품만, 나머지는 시리즈 시트에서)

## 카피 규칙
- 섹션 제목 옆에 사용법·설명 문구 넣지 않음 (예: "카테고리마다 최신 제품을 모았어요. 누르면…" → AI 티가 남)
- "N개 제품" 같은 자잘한 부가 정보, "~가 안 되면 ~하세요" 같은 안내성 작은 글 넣지 않음
- 제목은 직관적으로(고객 지원, 용도별 추천). 감성 문구(사는 순간부터, 쓰는 내내) 쓰지 않음

## 데이터 출처
- 가격·상품 링크: AVX 자사몰 ZOOM 브랜드관 https://www.avx.co.kr/goods/brand?code=0004 (2026-11 확인)
  - H6studio 699,000 · H5studio 659,000 · H6essential 559,000 · H4essential 399,000 · H2essential 339,000 · H1essential 199,000
  - F8n Pro 1,700,000 · F6 1,030,000 · F3 530,000 · G2 FOUR 357,000 · B2 FOUR 446,000 · MS-70CDR+ 214,000 · V6-SP 660,000 · V3 499,000
  - LiveTrak L12next 1,150,000 · L6max 570,000 · R20 891,000 · PodTrak P4next 305,000 · P2 199,000 · NEURIG 가격 문의(국내 안전 인증 진행 중)
- 자료실: AVX '메뉴얼 및 펌웨어' 게시판 https://www.avx.co.kr/board/?id=notice
- 기술 상담: AVX 카카오톡 채널 https://pf.kakao.com/_vXeNxj/chat · 전화 02-2265-0032 (평일 09:30–18:30, 점심 12:30–13:30, 토·일·공휴일 휴무)
- A/S 안내: AVX 자주 묻는 질문 https://www.avx.co.kr/board/?id=faq (수리 문의 시 필요한 정보 7가지, 발송 전 담당자 통화, 7일 이내 하자 외 발송 택배비 고객 부담·수리 후 반송비 AVX 부담)
- 제품 이미지: zoomcorp.com 공식 목록 이미지(투명 PNG), 일부는 Adobe 배경 제거
- 브랜드 컬러·톤 참고: 노션 'AVX ZOOM 인스타 디자인 지침 (2026-11-16 최신)', 'AVX ZOOM 인스타 계정 기획서'

## 남은 일
- 정식 ZOOM 로고 파일 반영 (지금은 글자로 임시 처리)
- 대표 제품 확정 (이펙터 대표를 출시 전인 NEURIG로 둘지, 판매 중인 G2 FOUR로 둘지)
- 자료실 '최근 자료' 목록은 수동 입력 → 실제 홈페이지 구축 시 게시판 연동 필요
- 브랜드명·로고 사용 범위 ZOOM 본사 확인 (계정 기획서의 본사 확인 사항)
- H6studio 상세페이지: 세로 하이라이트 사진 2장(S02·S03), 포맷 스위치 클로즈업(S09) 촬영 필요

## 이어서 작업하는 법
- 클라우드: claude.ai/code에서 새 세션 → 저장소 `melzyhouse/h6studio-page` 선택 → 하고 싶은 일만 말하기
- 홈페이지 수정: `zoom-audio-bento/make_page.py`(제품·카테고리 데이터) / `template.html`(레이아웃) → `python3 make_page.py && python3 build.py`
