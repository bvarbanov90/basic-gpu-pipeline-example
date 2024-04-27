@echo off
setlocal
set PS_SCRIPT=%~dp0download_texture.ps1

if not exist "%PS_SCRIPT%" (
    echo Could not find %PS_SCRIPT%
    exit /b 1
)

powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%PS_SCRIPT%" %*
if errorlevel 1 (
    echo Failed to download texture.
    exit /b %errorlevel%
)
endlocal
