@echo off
REM Script to check BOM dependency versions
REM Usage: check_version.bat

REM Save current directory
set CURRENT_DIR=%CD%

REM Move to project root directory (parent of tools folder)
cd /d "%~dp0.."

REM Execute Python script from tools folder
python "%~dp0check_version.py" %*

REM Restore current directory
cd /d "%CURRENT_DIR%"
