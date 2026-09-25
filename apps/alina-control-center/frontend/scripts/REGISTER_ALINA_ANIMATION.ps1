# ============================================================
# FATHER — AI ENGINEERING PLATFORM
# ПРОЕКТ: ALINA Control Center
# МОДУЛЬ: P3 Skeletal Animation Asset Registry
# ЭТАП: local animation verification
# СТАТУС: operator utility
# ВЕТКА: feature/father-knowledge-formation-standard-v01
# ============================================================

param(
  [Parameter(Mandatory=$true)][ValidateSet('IDLE_NEUTRAL','WALK_FORWARD','PRESENT_NEUTRAL')][string]$Intent,
  [Parameter(Mandatory=$true)][string]$File,
  [Parameter(Mandatory=$true)][string]$Source,
  [Parameter(Mandatory=$true)][string]$License
)

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$AssetDir = Join-Path $Root 'public\assets\agents\alina\animations'
$ManifestPath = Join-Path $Root 'public\assets\agents\alina\animation-manifest.json'

if (-not (Test-Path -LiteralPath $File -PathType Leaf)) { throw 'Animation file does not exist: ' + $File }
if ([IO.Path]::GetExtension($File).ToLowerInvariant() -ne '.vrma') { throw 'Only reviewed .vrma files are accepted by this utility.' }
if (-not (Test-Path -LiteralPath $ManifestPath -PathType Leaf)) { throw 'Animation manifest not found: ' + $ManifestPath }

New-Item -ItemType Directory -Force -Path $AssetDir | Out-Null
$TargetName = $Intent.ToLowerInvariant() + '.vrma'
$Target = Join-Path $AssetDir $TargetName
Copy-Item -LiteralPath $File -Destination $Target -Force
$Hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Target).Hash.ToLowerInvariant()

$Manifest = Get-Content -Raw -LiteralPath $ManifestPath | ConvertFrom-Json
$Record = $Manifest.assets.$Intent
$Record.status = 'LOCAL_VERIFIED'
$Record.path = '/assets/agents/alina/animations/' + $TargetName
$Record.source = $Source
$Record.license = $License
$Record.sha256 = $Hash
$Manifest | ConvertTo-Json -Depth 10 | Set-Content -Encoding utf8 -LiteralPath $ManifestPath

Write-Host ('Registered: ' + $Intent)
Write-Host ('Local path: ' + $Record.path)
Write-Host ('SHA-256: ' + $Hash)
Write-Host ('Manifest: ' + $ManifestPath)
