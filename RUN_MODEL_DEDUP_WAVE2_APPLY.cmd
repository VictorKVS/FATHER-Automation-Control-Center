@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo FATHER Model Dedup - Wave 2A APPLY
echo ============================================================
echo.
echo This command preserves every target path and replaces only
echo SHA-256 verified duplicates on G: with NTFS hardlinks.
echo Current standalone ComfyUI and MindForge resource trees are protected.
echo.

python -m py_compile scripts\model_dedup_wave1.py scripts\model_dedup_wave2.py
if errorlevel 1 goto :fail

python scripts\model_dedup_wave2.py --mode apply --confirm APPLY_WAVE2_HARDLINKS
if errorlevel 1 goto :fail

echo.
echo APPLIED. Review:
echo   reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.md
echo   reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.json
echo.
exit /b 0

:fail
echo.
echo ERROR/BLOCKED: Wave 2A apply stopped with exit code %errorlevel%.
exit /b %errorlevel%
