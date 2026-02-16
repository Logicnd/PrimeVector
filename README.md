# PrimeVector

PrimeVector is a **mobile-first AI automation** project that helps you build practical, reusable workflows powered by modern language models. The project is designed as a clean Python scaffold for creating prompt-driven utilities, automation scripts, and task orchestration patterns that can be triggered from mobile-friendly interfaces in the future.

## Vision

PrimeVector focuses on:

- AI-assisted task automation for everyday workflows.
- Reusable prompt templates and automation building blocks.
- A modular architecture that can grow into mobile-integrated tooling.

## Project Structure

```text
PrimeVector/
├── docs/
│   └── overview.md
├── examples/
│   └── run_prompt_example.py
├── src/
│   ├── ai_core/
│   │   └── model_runner.py
│   ├── automations/
│   │   └── simple_web_fetch.py
│   └── utils/
│       └── config.py
├── tests/
│   ├── test_ai_core_placeholder.py
│   └── test_automation_placeholder.py
└── requirements.txt
```

## Setup

### 1) Python version

Use **Python 3.10+** (recommended: 3.11).

### 2) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Usage

### Run the AI prompt example

```bash
python examples/run_prompt_example.py
```

### Example snippet

```python
from src.ai_core.model_runner import run_prompt

result = run_prompt("Summarize the benefits of mobile-first automation in three bullet points.")
print(result)
```

## Next Steps

- Add prompt template management in `src/ai_core/`.
- Implement richer automation flows in `src/automations/`.
- Build API or UI layers for mobile and cross-platform interactions.
