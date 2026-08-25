@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo FATHER Model Dedup - Wave 1 PLAN ONLY (READ ONLY)
echo ============================================================
echo.
echo This command DOES NOT modify model files.
echo It selects exact SHA-256 duplicates eligible for path-preserving
echo NTFS hardlink consolidation on G:.
echo.

python scripts\model_dedup_wave1.py --mode plan
if errorlevel 1 goto :fail

echo.
echo DONE. Review:
echo   reports\model_inventory\consolidation_wave1\wave1_hardlink_plan.md
echo   reports\model_inventory\consolidation_wave1\wave1_hardlink_plan.json
echo.
exit /b 0

:fail
echo.
echo ERROR: Wave 1 planning stopped with exit code %errorlevel%.
exit /b %errorlevel%
