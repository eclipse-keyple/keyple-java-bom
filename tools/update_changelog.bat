@echo off
REM Script to update CHANGELOG.md
REM Usage: update_changelog.bat [YYYY.MM.DD]

REM Save current directory
set CURRENT_DIR=%CD%

REM Move to project root directory (parent of tools folder)
cd /d "%~dp0.."

REM Execute Python script from tools folder
python "%~dp0update_changelog.py" %*

REM Restore current directory
cd /d "%CURRENT_DIR%"
