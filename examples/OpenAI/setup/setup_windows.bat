@echo off
REM setup_windows.bat — create the deitel-openai conda environment on Windows
REM Run from the repo root in Anaconda Prompt:  setup\setup_windows.bat

set "SCRIPT_DIR=%~dp0"
for %%I in ("%SCRIPT_DIR%..") do set "REPO_ROOT=%%~fI"
set "CODEX_TEMPLATE_DIR=%REPO_ROOT%\codex-demos-template"
set "CODEX_DEMOS_DIR=%REPO_ROOT%\codex-demos"
set "ENVIRONMENT_FILE=%SCRIPT_DIR%environment.yml"

echo === Preparing Codex demos workspace ===
echo Template: "%CODEX_TEMPLATE_DIR%"
echo Target:   "%CODEX_DEMOS_DIR%"
if exist "%CODEX_DEMOS_DIR%\" (
    echo codex-demos already exists; leaving it unchanged.
) else (
    if not exist "%CODEX_TEMPLATE_DIR%\" (
        echo ERROR: codex-demos-template was not found.
        exit /b 1
    )
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Copy-Item -LiteralPath '%CODEX_TEMPLATE_DIR%' -Destination '%CODEX_DEMOS_DIR%' -Recurse -Force"
    if errorlevel 1 (
        echo ERROR: failed to copy codex-demos-template to codex-demos.
        exit /b 1
    )
    if not exist "%CODEX_DEMOS_DIR%\AGENTS.md" (
        echo ERROR: codex-demos was created, but expected files were not copied.
        exit /b 1
    )
    echo Created codex-demos from codex-demos-template.
    echo codex-demos is ignored by Git so students can initialize it separately.
)

echo.
echo === Creating conda environment 'deitel-openai' ===
conda env create -f "%ENVIRONMENT_FILE%"
if errorlevel 1 (
    echo ERROR: conda env create failed.
    exit /b 1
)

echo.
echo === Activating environment ===
call conda activate deitel-openai
if errorlevel 1 (
    echo ERROR: conda activate failed.
    exit /b 1
)
if /I not "%CONDA_DEFAULT_ENV%"=="deitel-openai" (
    echo ERROR: expected deitel-openai to be active, but CONDA_DEFAULT_ENV is "%CONDA_DEFAULT_ENV%".
    exit /b 1
)
echo Active Conda environment: %CONDA_DEFAULT_ENV%
python -c "import sys; print('Python executable:', sys.executable)"

echo.
echo === Installing Playwright browser (Chromium) ===
python -m playwright install chromium
if errorlevel 1 (
    echo ERROR: playwright install failed.
    exit /b 1
)

echo.
echo === Installing spaCy English model ===
python -m spacy download en_core_web_sm
if errorlevel 1 (
    echo ERROR: spaCy English model install failed.
    exit /b 1
)

echo.
echo === Verifying realtime voice dependencies ===
python -c "import sounddevice; print('sounddevice OK')"
if errorlevel 1 (
    echo ERROR: sounddevice import failed.
    exit /b 1
)

echo.
echo === Registering the Jupyter kernel ===
python -m ipykernel install --user --name deitel-openai --display-name "Python (deitel-openai)"
if errorlevel 1 (
    echo ERROR: Jupyter kernel registration failed.
    exit /b 1
)

echo.
echo ============================================================
echo  Setup complete!
echo.
echo  To start working, open Anaconda Prompt and run:
echo    conda activate deitel-openai
echo    cd /d "%REPO_ROOT%"
echo    jupyter lab
echo ============================================================
