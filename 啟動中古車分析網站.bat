@echo off
chcp 65001 >nul
cd /d "%~dp0"
python -u scripts\analyze_market.py --serve --port 8000
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python server failed to start. Please check Python installation.
    pause
)
