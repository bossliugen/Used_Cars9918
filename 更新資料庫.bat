@echo off
chcp 65001 >nul
cd /d "%~dp0"
python -u scripts\analyze_market.py --build-only
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Update failed. Please check Python installation.
)
pause
