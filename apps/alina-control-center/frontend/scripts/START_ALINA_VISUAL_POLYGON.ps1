# ============================================================
# FATHER — AI ENGINEERING PLATFORM
# ПРОЕКТ: ALINA Control Center
# МОДУЛЬ: P3 Visual Polygon
# ЭТАП: local procedural pose / locomotion review
# СТАТУС: operator launcher
# ВЕТКА: feature/father-knowledge-formation-standard-v01
# ============================================================

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Avatar = Join-Path $Root 'public\assets\agents\alina\Seed-san.vrm'
if (-not (Test-Path -LiteralPath $Avatar -PathType Leaf)) {
  throw 'Seed-san.vrm is missing. Run the verified avatar acquisition step first.'
}

Write-Host 'ALINA P3 visual polygon'
Write-Host '1. Open the local URL printed by Vite.'
Write-Host '2. Confirm ALINA arms are lowered from T-pose.'
Write-Host '3. Click the 3D humanoid once.'
Write-Host '4. Observe alternating arms/legs while she moves to INFORMATION_WALL.'
Write-Host '5. Capture a screenshot before movement and after arrival.'
Write-Host ''
Write-Host 'Starting Vite...'
npm run dev
