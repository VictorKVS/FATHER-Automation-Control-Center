@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo FATHER Model Factory - Local Model Inventory v2 (READ ONLY)
echo ============================================================
echo.

set "PY=python"
%PY% --version
if errorlevel 1 goto :fail

if not exist "reports\model_inventory\generated" mkdir "reports\model_inventory\generated"

echo Scanning local fixed/removable drives.
echo No files will be moved or deleted.
echo Python venv/site-packages/test fixtures are excluded.
echo Discovery report is saved BEFORE SHA-256 hashing.
echo SHA-256 is calculated only for duplicate candidates >= 64 MiB by default.
echo.

%PY% scripts\model_inventory_v2.py --hash duplicates --min-hash-mib 64 --output "reports\model_inventory\generated"
if errorlevel 1 goto :fail

echo.
echo DONE.
echo Review:
echo   reports\model_inventory\generated\model_inventory.md
echo   reports\model_inventory\generated\model_inventory.json
echo   reports\model_inventory\generated\model_dedup_plan.json
echo.
exit /b 0

:fail
echo.
echo NOTE: if hashing was interrupted, the discovery report may still exist.
echo Review:
echo   reports\model_inventory\generated\model_inventory.md
echo ERROR: model inventory stopped with exit code %errorlevel%.
exit /b %errorlevel%
