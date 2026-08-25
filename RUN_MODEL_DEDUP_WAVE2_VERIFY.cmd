@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo FATHER Model Dedup - Wave 2A IMAGE VERIFY (READ ONLY)
echo ============================================================
echo.
echo This command recomputes SHA-256 for every selected target and
echo canonical survivor. It DOES NOT modify, move, link or delete files.
echo.

python -m py_compile scripts\model_dedup_wave2.py
if errorlevel 1 goto :fail

python scripts\model_dedup_wave2.py --mode verify
if errorlevel 1 goto :fail

echo.
echo VERIFIED. Review:
echo   reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.md
echo.
exit /b 0

:fail
echo.
echo ERROR/BLOCKED: Wave 2A verification stopped with exit code %errorlevel%.
exit /b %errorlevel%
