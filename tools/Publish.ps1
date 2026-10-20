# Publishes this exact local documentation package to the user's existing repository.
# Run explicitly: powershell -ExecutionPolicy Bypass -File .\tools\Publish.ps1
# No credentials are embedded. No force push, reset, deletion, or Pages setting change.
[CmdletBinding()]
param([switch]$Yes)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$ExpectedRemote = 'https://github.com/techsoftye/CodexStudio-.git'
$PackageRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..')).TrimEnd('\', '/')
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git is not installed or is not available on PATH.'
}
function Invoke-Git {
    param([Parameter(Mandatory = $true)][string[]]$Arguments)
    & git @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw ('git ' + ($Arguments -join ' ') + ' failed. No further steps were performed.')
    }
}
Push-Location $PackageRoot
try {
    foreach ($Required in @('README.md', 'index.html', 'article\Article-EN.md', 'full_RFC\EN\Codex_Studio_Full_RFC_EN.md')) {
        if (-not (Test-Path -LiteralPath (Join-Path $PackageRoot $Required))) {
            throw "Missing package file: $Required. Extract the complete ZIP first."
        }
    }
    # Do not accidentally initialize inside another, unrelated project.
    $Parent = Split-Path $PackageRoot -Parent
    while ($Parent) {
        if (Test-Path -LiteralPath (Join-Path $Parent '.git')) {
            throw 'The package is inside another Git repository. Move it to a separate folder first.'
        }
        $NextParent = Split-Path $Parent -Parent
        if ($NextParent -eq $Parent) { break }
        $Parent = $NextParent
    }
    if (-not (Test-Path -LiteralPath (Join-Path $PackageRoot '.git'))) {
        Invoke-Git -Arguments @('init', '-b', 'main')
    }
    $ActualRoot = (& git rev-parse --show-toplevel).Trim()
    if ($LASTEXITCODE -ne 0) { throw 'Cannot resolve repository root.' }
    if ([System.IO.Path]::GetFullPath($ActualRoot).TrimEnd('\', '/') -ine $PackageRoot) {
        throw 'Git root is not the package folder. Stopping to avoid publishing another project.'
    }
    $Branch = (& git symbolic-ref --short HEAD).Trim()
    if ($LASTEXITCODE -ne 0 -or $Branch -ne 'main') {
        throw 'The local branch must be main. Resolve the branch choice yourself before running this script.'
    }
    $Remotes = @(& git remote)
    if ($LASTEXITCODE -ne 0) { throw 'Cannot list Git remotes.' }
    if ($Remotes -contains 'origin') {
        $Origin = (& git remote get-url origin).Trim()
        if ($LASTEXITCODE -ne 0) { throw 'Cannot read origin URL.' }
        if ($Origin -notin @($ExpectedRemote, 'https://github.com/techsoftye/CodexStudio-', 'git@github.com:techsoftye/CodexStudio-.git')) {
            throw "Origin points elsewhere: $Origin. No remote was changed."
        }
    } else {
        Invoke-Git -Arguments @('remote', 'add', 'origin', $ExpectedRemote)
    }
    $Name = & git config user.name
    $NameExit = $LASTEXITCODE
    $Email = & git config user.email
    $EmailExit = $LASTEXITCODE
    if ($NameExit -ne 0 -or $EmailExit -ne 0 -or [string]::IsNullOrWhiteSpace($Name) -or [string]::IsNullOrWhiteSpace($Email)) {
        throw 'Configure your own Git user.name and user.email (or your GitHub noreply email), then run again. No identity is invented here.'
    }
    Write-Host "Folder: $PackageRoot"
    Write-Host "Destination: $ExpectedRemote"
    Write-Host 'This package and its mockups will become publicly readable after the push.'
    Invoke-Git -Arguments @('status', '--short')
    if (-not $Yes) {
        $Reply = Read-Host 'Type PUBLISH to stage, commit, and push these files'
        if ($Reply -cne 'PUBLISH') { Write-Host 'Cancelled. Nothing was committed or pushed.'; return }
    }
    Invoke-Git -Arguments @('add', '--all', '.')
    & git diff --cached --quiet
    $DiffExit = $LASTEXITCODE
    if ($DiffExit -eq 1) {
        Invoke-Git -Arguments @('commit', '-m', 'Publish Codex Studio proposal and bilingual RFC draft')
    } elseif ($DiffExit -ne 0) {
        throw 'Cannot inspect staged changes.'
    }
    Invoke-Git -Arguments @('push', '-u', 'origin', 'main')
    Write-Host 'Push succeeded. Configure GitHub Pages separately: main / (root).'
    Write-Host 'See publication\UPLOAD-AR.md for the exact Pages settings.'
} finally {
    Pop-Location
}
