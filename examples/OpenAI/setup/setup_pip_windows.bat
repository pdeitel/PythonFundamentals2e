@echo off
REM setup_pip_windows.bat — create a pip virtual environment on Windows
REM Requires Python 3.14 or later already installed and on PATH.
REM Run from the repo root in Command Prompt or PowerShell:
REM   setup\setup_pip_windows.bat

set "SCRIPT_DIR=%~dp0"
for %%I in ("%SCRIPT_DIR%..") do set "REPO_ROOT=%%~fI"
set "CODEX_TEMPLATE_DIR=%REPO_ROOT%\codex-demos-template"
set "CODEX_DEMOS_DIR=%REPO_ROOT%\codex-demos"
set "REQUIREMENTS_FILE=%SCRIPT_DIR%requirements.txt"
set "VENV_PYTHON=%REPO_ROOT%\.venv\Scripts\python.exe"

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
echo === Checking Python version ===
python --version
if errorlevel 1 (
    echo ERROR: Python not found. Install Python 3.14+ from https://python.org
    exit /b 1
)
python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 14) else 1)"
if errorlevel 1 (
    echo ERROR: Python 3.14 or later is required. Install Python 3.14+ from https://python.org
    exit /b 1
)

echo.
echo === Checking Graphviz ===
where dot >nul 2>nul
if errorlevel 1 (
    echo ERROR: Graphviz is required for Agents SDK graph visualizations.
    echo Install Graphviz from https://graphviz.org/download/ and make sure dot.exe is on PATH.
    exit /b 1
)
dot -V

echo.
echo === Creating virtual environment at .venv ===
python -m venv .venv
if errorlevel 1 (
    echo ERROR: venv creation failed.
    exit /b 1
)

echo.
echo === Activating virtual environment ===
call .venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: venv activation failed.
    exit /b 1
)

echo.
echo === Installing packages ===
"%VENV_PYTHON%" -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: pip upgrade failed.
    exit /b 1
)
"%VENV_PYTHON%" -m pip install -r "%REQUIREMENTS_FILE%"
if errorlevel 1 (
    echo ERROR: pip install failed.
    exit /b 1
)

echo.
echo === Installing Playwright browser (Chromium) ===
"%VENV_PYTHON%" -m playwright install chromium
if errorlevel 1 (
    echo ERROR: playwright install failed.
    exit /b 1
)

echo.
echo === Installing spaCy English model ===
"%VENV_PYTHON%" -m spacy download en_core_web_sm
if errorlevel 1 (
    echo ERROR: spaCy English model install failed.
    exit /b 1
)

echo.
echo === Verifying realtime voice dependencies ===
"%VENV_PYTHON%" -c "import sounddevice; print('sounddevice OK')"
if errorlevel 1 (
    echo ERROR: sounddevice import failed.
    exit /b 1
)

echo.
echo === Registering the Jupyter kernel ===
"%VENV_PYTHON%" -m ipykernel install --user --name deitel-openai --display-name "Python (deitel-openai)"
if errorlevel 1 (
    echo ERROR: Jupyter kernel registration failed.
    exit /b 1
)

echo.
echo ============================================================
echo  Setup complete!
echo.
echo  To start working, open a new Command Prompt and run:
echo    .venv\Scripts\activate
echo    cd /d "%REPO_ROOT%"
echo    jupyter lab
echo ============================================================
