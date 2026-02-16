# Runs a basic PrimeVector AI prompt example from the command line.

from __future__ import annotations

from src.ai_core.openai_client import run_prompt


def main() -> None:
    """Execute a sample prompt and print the model response."""
    prompt = "Give 3 concise ideas for mobile-first AI task automation."
    response = run_prompt(prompt)
    print("Prompt:", prompt)
    print("Response:", response)


if __name__ == "__main__":
    main()
