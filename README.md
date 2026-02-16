# PrimeVector

PrimeVector is a **mobile-first AI automation** starter project for building lightweight, scriptable workflows powered by large language models. It is designed for teams and builders who want to prototype task automation quickly and then evolve those automations into production-ready services.

## Vision

PrimeVector focuses on:

- **AI-driven task orchestration** with prompt-based workflows.
- **Mobile-first operating model** where workflows are easy to trigger from compact interfaces and notifications.
- **Composable architecture** so automations, model logic, and utility code remain modular.

## Project Structure

```text
PrimeVector/
├── docs/                 # Architecture notes and project documentation
├── examples/             # Runnable examples that showcase core functionality
├── src/
│   ├── ai_core/          # LLM/model wrapper logic
│   ├── automations/      # Automation workflow scripts and stubs
│   └── utils/            # Shared helper utilities
├── tests/                # Placeholder tests for future implementation
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python **3.11+**
- An OpenAI API key

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Set your OpenAI API key before running examples:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Example Usage

Run the included prompt example:

```bash
python examples/run_prompt_example.py
```

Expected behavior:

1. Loads the OpenAI client.
2. Sends a sample prompt.
3. Prints the model response.

You can also import the helper directly:

```python
from src.ai_core.openai_client import run_prompt

response = run_prompt("Summarize the benefits of mobile-first automation in 3 bullets.")
print(response)
```

## Next Steps

- Add domain-specific prompt templates in `src/ai_core/`.
- Implement automation workflows in `src/automations/`.
- Expand tests in `tests/` with integration and unit coverage.
