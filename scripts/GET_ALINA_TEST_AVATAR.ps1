# ============================================================
# FATHER — AI ENGINEERING PLATFORM
# ПРОЕКТ: ALINA Control Center
# МОДУЛЬ: Human Agent Studio / Temporary VRM Asset
# ЭТАП: P2 — local test avatar acquisition
# СТАТУС: TEST_ONLY
# ВЕТКА: feature/father-knowledge-formation-standard-v01
# ============================================================

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$TargetDir = Join-Path $RepoRoot "apps\alina-control-center\frontend\public\assets\agents\alina"
$Target = Join-Path $TargetDir "Seed-san.vrm"
$HashFile = Join-Path $TargetDir "Seed-san.sha256.txt"
$Source = "https://raw.githubusercontent.com/vrm-c/vrm-specification/master/samples/Seed-san/vrm/Seed-san.vrm"

New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null

Write-Host "FATHER / ALINA #001 — acquiring TEST_ONLY VRM asset"
Write-Host "Source: $Source"
Write-Host "Target: $Target"

Invoke-WebRequest -Uri $Source -OutFile $Target

$Hash = (Get-FileHash -Path $Target -Algorithm SHA256).Hash.ToLowerInvariant()
"$Hash  Seed-san.vrm" | Set-Content -Path $HashFile -Encoding utf8

Write-Host ""
Write-Host "Downloaded successfully."
Write-Host "SHA-256: $Hash"
Write-Host "Hash record: $HashFile"
Write-Host ""
Write-Host "IMPORTANT: Seed-san is a temporary polygon asset, not ALINA's permanent appearance."
Write-Host "License record: public/assets/agents/alina/asset-manifest.json"
