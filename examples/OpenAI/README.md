# Python OpenAI API, Agents SDK & the Codex App: A Code-Intensive Intro

In this  **presentation-only course**, I cover:

* OpenAI APIs via the official OpenAI Python SDK
* OpenAI Agents SDK
* OpenAI Codex app using Python and JupyterLab

Many attendees like to run examples in parallel. If you run into software issues during class, I will not have time to debug them live, but I am happy to help after class. E-mail me at paul@deitel.com.

---

## Pre-Class Checklist

Complete these steps (discussed below) to run the notebooks locally:

1. Install Anaconda or Python 3.14+.
2. Install the OpenAI Codex desktop app.
3. Get the course code from GitHub.
4. Run the setup script from the course folder.
5. Create and store your OpenAI API key in the `OPENAI_API_KEY` environment variable.
6. Launch JupyterLab from the course folder.

I'll briefly review these steps in the notebooks `00-03-software-setup.ipynb` and `00-04-openai-account-setup.ipynb` in class.

---

## Required Software

### Python

Recommended:

* [Anaconda](https://www.anaconda.com/download)

Alternative:

* Python 3.14+ from [python.org](https://www.python.org/downloads/), Homebrew, `pyenv`, or another Python distribution

**Note**  
* I tested the demos with Python 3.14
* AI assessments by OpenAI's Codex and Anthropic's Claude Code indicated that most examples should work with Python 3.10 or higher, but **I did not confirm**.

### OpenAI Codex Desktop App

Download and run the installer:

> https://developers.openai.com/codex/app

I used the default installation settings.

### Graphviz

Graphviz is used for Agents SDK graph visualizations.

* Anaconda setup installs Graphviz automatically.
* If you use `pip`/`venv`, install [Graphviz](https://graphviz.org/download/) separately and make sure the `dot` executable is on your `PATH`.

#### Internet Access

OpenAI APIs are online web services, so the API examples require Internet access. The Codex app also requires Internet access.

---

## Download the Course Code & Notebooks

Either download and unzip the repository from GitHub:

> https://github.com/pdeitel/Python-OpenAI-API-and-Intro-to-Agents-SDK

Then open a terminal in the unzipped folder.

Or clone the repository:

```bash
git clone https://github.com/pdeitel/Python-OpenAI-API-and-Intro-to-Agents-SDK.git
cd Python-OpenAI-API-and-Intro-to-Agents-SDK
```

All setup commands below must be run from the course's root folder: the folder that contains both `README.md` and the `setup/` folder.

---

## Setup — Anaconda Users (Recommended)

The setup script:

* creates a conda environment named `deitel-openai`
* installs the OpenAI Python SDK: `openai`
* installs the OpenAI Agents SDK with LiteLLM support: `openai-agents[litellm]`
* installs JupyterLab and registers the `Python (deitel-openai)` kernel
* installs Graphviz support for Agents SDK workflow visualizations
* installs Playwright Chromium browser support for the Computer Tool demo (if we have time)
* installs common data-science, visualization and NLP libraries such as `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `spacy` and `nltk` 
* verifies realtime voice dependencies (for a quick demo if we have time)
* copies `codex-demos-template/` to an ignored `codex-demos/` working folder if `codex-demos/` does not already exist

### macOS

```bash
bash setup/setup_mac.sh
```

### Windows

Open **Anaconda Prompt** or **Anaconda PowerShell**, navigate to the course folder, then run:

```bat
setup\setup_windows.bat
```

---

## Setup — Python/pip Users

**Use these instructions only if you are not using Anaconda. I did not test the pip setups—I simply asked Codex to mimic the Anaconda setups.**

### macOS / Linux

Install Graphviz first if needed:

```bash
# macOS with Homebrew
brew install graphviz

# Debian/Ubuntu Linux
sudo apt install graphviz
```

Then run this from the course folder:

```bash
bash setup/setup_pip_mac.sh
```

### Windows

Install Graphviz from [graphviz.org/download](https://graphviz.org/download/) first and make sure `dot.exe` is on your `PATH`.

Then open **Command Prompt** or **PowerShell**, navigate to the course folder, and run:

```bat
setup\setup_pip_windows.bat
```

The pip setup does not use Conda or the `deitel-openai` conda environment. It creates a local `.venv` virtual environment and installs packages into that environment.

---

## OpenAI Developer API Key

The OpenAI APIs are online web services and do not provide a free tier for API usage. To run the code, you need:

* an OpenAI developer account
* an OpenAI API key

### Get an API Key

1. Sign in at [platform.openai.com](https://platform.openai.com).
2. Go to the API keys page in your project settings.
3. Press **+ Create new secret key**.
4. Copy the key immediately. It is shown only once.

### Store the Key in an Environment Variable

The notebooks read your key from the `OPENAI_API_KEY` environment variable.

Do not paste API keys into notebooks or source files. OpenAI recommends keeping API keys secret, using environment variables rather than hardcoding keys, monitoring usage, and rotating keys if you suspect exposure:

> https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

### macOS / Linux

Add this line to `~/.zshrc` or `~/.bash_profile`, replacing `YourAPIKey` with your actual key:

```bash
export OPENAI_API_KEY="YourAPIKey"
```

Then reload the shell:

```bash
source ~/.zshrc
```

If you use a different shell startup file, update that file instead.

### Windows

1. Close any open Command Prompt, PowerShell or Anaconda Prompt windows.
2. In the taskbar's **Search** field, enter `SystemPropertiesAdvanced`, then press Enter.
3. In the **System Properties** dialog, press **Environment Variables...**.
4. Under **User variables**, press **New...**.
5. Variable name: `OPENAI_API_KEY`
6. Variable value: paste your API key.
7. Press **OK** to save, then press **OK** to close the dialog.
8. Open a new terminal before launching JupyterLab.

---

## Launch JupyterLab From the Course Folder

### Anaconda

```bash
conda activate deitel-openai
jupyter lab
```

If a notebook does not have a kernel selected, choose the **Python (deitel-openai)** kernel.

### Python/pip on macOS / Linux

```bash
source .venv/bin/activate
jupyter lab
```

### Python/pip on Windows

```bat
.venv\Scripts\activate
jupyter lab
```

---

## OPTIONAL Setup for `02-05-09` — Local LLM via LiteLLM + Ollama 

This demo runs an open-source LLM model locally rather than using a hosted OpenAI model, showing that the OpenAI Agents SDK is model agnostic. 

**The model is approximately an 8 GB download so this is entirely optional.** The demo was tested on a MacBook Pro M2 Max with 96 GB of unified memory. On less powerful hardware, inference will be significantly slower and tool-calling reliability may vary.

1. Install [Ollama](https://ollama.com/download).
2. Pull the model used in the demo:
   ```bash
   ollama pull deepseek-r1:14b
   ```
3. Start Ollama before running the notebook:
   ```bash
   ollama serve
   ```

---

## Troubleshooting

**`OPENAI_API_KEY` not found** — Restart your terminal, Anaconda Prompt, PowerShell or JupyterLab after setting the environment variable. JupyterLab inherits environment variables from the shell that launched it.

**`conda activate` not recognized on macOS** — Initialize conda for your shell: `conda init zsh` or `conda init bash`, then open a new terminal.

**Graphviz `dot` not found** — Install Graphviz and make sure the `dot` command is on your `PATH`. The Anaconda setup installs Graphviz automatically; the `pip`/`venv` setup checks for it before creating the environment.

**Audio playback in `01-02-speech.ipynb` does not work** — Listen to the generated audio files directly from the `resources/outputs/` folder with your system's audio player.

**Playwright browser does not launch** — Run `playwright install chromium` again from the activated environment, then retry.

**Local LLMs running in Ollama can be slow in `02-05-09`** — This is expected on most consumer hardware. The demo is illustrative.

---

&copy; 2026 by Deitel & Associates, Inc. All Rights Reserved.
