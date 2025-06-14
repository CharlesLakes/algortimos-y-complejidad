@echo off
setlocal enabledelayedexpansion

REM Directorio de instalación en el perfil del usuario
set "MINGW_DIR=%USERPROFILE%\mingw"

REM URL de la versión portable de MinGW-w64
set "MINGW_URL=https://github.com/brechtsanders/winlibs_mingw/releases/download/15.1.0posix-13.0.0-ucrt-r2/winlibs-x86_64-posix-seh-gcc-15.1.0-mingw-w64ucrt-13.0.0-r2.zip"
set "MINGW_ZIP=%TEMP%\mingw.zip"

echo Descargando MinGW desde:
echo !MINGW_URL!

curl -L -o "!MINGW_ZIP!" "!MINGW_URL!"
if errorlevel 1 (
    echo ❌ Error al descargar MinGW.
    exit /b 1
)

echo ✅ Descarga completada.

echo Extrayendo MinGW en !MINGW_DIR!...
mkdir "!MINGW_DIR!" >nul 2>&1
tar -xf "!MINGW_ZIP!" -C "!MINGW_DIR!" --strip-components=1

if errorlevel 1 (
    echo ❌ Error al extraer MinGW.
    exit /b 1
)

del "!MINGW_ZIP!" >nul

REM Agregar bin al PATH del usuario
set "MINGW_BIN=!MINGW_DIR!\bin"
setx PATH "%PATH%;!MINGW_BIN!"

echo ✅ MinGW instalado en: !MINGW_DIR!
echo 🔄 Cierra y vuelve a abrir el CMD para que el PATH se actualice.

echo Probando instalación:
"!MINGW_BIN!\g++" --version

pause
