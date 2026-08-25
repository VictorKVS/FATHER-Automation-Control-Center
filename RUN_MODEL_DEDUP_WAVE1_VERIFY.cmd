@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo FATHER Model Dedup - Wave 1 VERIFY (READ ONLY)
echo ============================================================
echo.
echo This command recomputes SHA-256 for every Wave 1 target and its
echo canonical survivor. It DOES NOT modify, move, link or delete files.
echo.

python -m py_compile scripts\model_dedup_wave1.py
if errorlevel 1 goto :fail

python scripts\model_dedup_wave1.py --mode verify
if errorlevel 1 goto :fail

echo.
echo VERIFIED. Review:
echo   reports\model_inventory\consolidation_wave1\wave1_hardlink_plan.md
echo.
exit /b 0

:fail
echo.
echo ERROR/BLOCKED: Wave 1 verification stopped with exit code %errorlevel%.
exit /b %errorlevel%
