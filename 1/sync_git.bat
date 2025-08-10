@echo off
echo ================================
echo Git 자동 동기화 스크립트 실행
echo ================================

git status

echo.

echo 모든 변경 사항 스테이지에 올리기...
git add .

set /p commitmsg=커밋 메시지를 입력하세요: 
if "%commitmsg%"=="" (
    echo 커밋 메시지가 비어있습니다. 기본 메시지 사용: "Auto commit"
    set commitmsg=Auto commit
)

git commit -m "%commitmsg%"

echo 원격 저장소에서 최신 내용 가져오기 (rebase)...
git pull --rebase

echo 원격 저장소에 변경사항 푸시 중...
git push

echo.
echo 작업 완료!
pause
