@echo off
chcp 65001 >nul
title 更新中古車行情資料庫 (GitHub Pages 靜態輸出)
cd /d "%~dp0"

echo 正在執行 Python 重新計算並更新 data\cars_db.json ...
python scripts\analyze_market.py --build-only

if %errorlevel% equ 0 (
    echo.
    echo 更新完成！您現在可以將 data\cars_db.json 推送至 GitHub Pages。
) else (
    echo.
    echo [錯誤] 更新失敗，請確認 Python 環境。
)
pause
