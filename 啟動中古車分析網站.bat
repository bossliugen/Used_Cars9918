@echo off
chcp 65001 >nul
title 台灣中古車時價分析與世代通病資料庫
cd /d "%~dp0"

echo ========================================================
echo   台灣中古車時價分析與世代通病資料庫 - Python 分析引擎
echo ========================================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [錯誤] 找不到 Python，請先安裝 Python 3.8 以上版本並加入 PATH。
    pause
    exit /b 1
)

echo [1/2] 正在透過 Python 重新計算各世代折舊曲線與行情資料庫...
echo [2/2] 啟動本地網頁伺服器並自動開啟瀏覽器...
echo.
python scripts\analyze_market.py --serve --port 8000

if %errorlevel% neq 0 (
    echo.
    echo [錯誤] 程式執行發生異常，請檢查上方錯誤訊息。
    pause
)
