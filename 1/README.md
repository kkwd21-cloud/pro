# 자동 영상 제작 프로젝트

## 개요
이 프로젝트는 음악 파일과 이미지 파일을 입력 받아  
자동으로 영상으로 합성하는 웹 기반 자동화 도구입니다.

## 프로젝트 구조
- frontend/ : 웹 UI (HTML, CSS, JS)
- backend/ : 영상 합성용 Python + FFmpeg 스크립트
- README.md : 설명서 및 실행 방법

## 실행 환경
- Python 3.8 이상
- FFmpeg 설치 및 환경 변수 등록 필요
- 최신 웹 브라우저 권장 (Chrome, Edge 등)

## 실행 방법

1. backend 폴더로 이동
2. `python main.py` 실행 (영상 합성 서버 시작)
3. frontend 폴더에서 index.html을 브라우저로 열거나, 간단한 웹 서버에서 실행
4. 웹 UI에서 음악과 이미지 업로드 후 영상 생성 버튼 클릭

## 주의사항
- FFmpeg가 설치되어 있어야 정상 작동합니다.
- Python 패키지 설치: `pip install flask`

---
