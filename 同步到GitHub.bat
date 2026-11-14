@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WinGet\Packages\Git.MinGit_Microsoft.Winget.Source_8wekyb3d8bbwe\cmd"

echo [1/3] Rebuilding data\cars_db.json via Python...
python -u scripts\analyze_market.py --build-only
if %errorlevel% neq 0 (
    echo [ERROR] Python build failed.
    pause
    exit /b 1
)

echo [2/3] Staging and committing changes...
git add .
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo [INFO] No local changes to commit. Pushing latest branch just in case...
) else (
    git commit -m "chore: update used car market database"
)

echo [3/3] Pushing to GitHub (origin main)...
git push origin main
if %errorlevel% equ 0 (
    echo.
    echo [DONE] Synced to GitHub! GitHub Pages will update in ~1 minute.
) else (
    echo.
    echo [ERROR] Git push failed. Please check network or GitHub login.
)
pause
