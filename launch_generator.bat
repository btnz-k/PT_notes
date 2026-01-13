@echo off
REM Pentest Engagement Generator Launcher

echo.
echo ==========================================
echo   Pentest Engagement Generator
echo ==========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [INFO] Starting Engagement Generator...
python "%~dp0scripts\engagement_generator.py"

if errorlevel 1 (
    pause
)
