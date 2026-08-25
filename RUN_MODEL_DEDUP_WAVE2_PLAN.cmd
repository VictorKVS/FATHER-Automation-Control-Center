@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo FATHER Model Dedup - Wave 2A IMAGE PLAN ONLY (READ ONLY)
echo ============================================================
echo.
echo This command DOES NOT modify model files.
echo It plans exact SHA-256 duplicate consolidation only in old image-model trees.
echo.

python -m py_compile scripts\model_dedup_wave2.py
if errorlevel 1 goto :fail

python scripts\model_dedup_wave2.py --mode plan
if errorlevel 1 goto :fail

echo.
echo DONE. Review:
echo   reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.md
echo   reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.json
echo.
exit /b 0

:fail
echo.
echo ERROR/BLOCKED: Wave 2A planning stopped with exit code %errorlevel%.
exit /b %errorlevel%
