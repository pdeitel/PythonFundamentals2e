#!/usr/bin/env bash
# setup_mac.sh — create the deitel-openai conda environment on macOS
# Run from the repo root:  bash setup/setup_mac.sh

set -e  # stop on first error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CODEX_TEMPLATE_DIR="$REPO_ROOT/codex-demos-template"
CODEX_DEMOS_DIR="$REPO_ROOT/codex-demos"

prepare_codex_demos() {
    echo ""
    echo "=== Preparing Codex demos workspace ==="
    if [ -d "$CODEX_DEMOS_DIR" ]; then
        echo "codex-demos already exists; leaving it unchanged."
        return
    fi
    if [ ! -d "$CODEX_TEMPLATE_DIR" ]; then
        echo "ERROR: codex-demos-template was not found."
        exit 1
    fi
    cp -R "$CODEX_TEMPLATE_DIR" "$CODEX_DEMOS_DIR"
    echo "Created codex-demos from codex-demos-template."
    echo "codex-demos is ignored by Git so students can initialize it separately."
}

echo "=== Creating conda environment 'deitel-openai' ==="
conda env create -f "$SCRIPT_DIR/environment.yml"

echo ""
echo "=== Activating environment ==="
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate deitel-openai

echo ""
echo "=== Installing Playwright browser (Chromium) ==="
playwright install chromium

echo ""
echo "=== Installing spaCy English model ==="
python -m spacy download en_core_web_sm

echo ""
echo "=== Verifying realtime voice dependencies ==="
python -c "import sounddevice; print('sounddevice OK')"

echo ""
echo "=== Registering the Jupyter kernel ==="
python -m ipykernel install --user --name deitel-openai --display-name "Python (deitel-openai)"

prepare_codex_demos

echo ""
echo "============================================================"
echo " Setup complete!"
echo ""
echo " To start working:"
echo "   conda activate deitel-openai"
echo "   cd $REPO_ROOT"
echo "   jupyter lab"
echo "============================================================"
