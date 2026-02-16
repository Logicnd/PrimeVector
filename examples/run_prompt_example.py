"""Runnable example script showing how to call the PrimeVector AI prompt runner."""

from __future__ import annotations

from src.ai_core.model_runner import run_prompt


def main() -> None:
    """Execute a sample prompt and print the response."""
    sample_prompt = "Provide 3 quick ideas for mobile-first AI automations."
    output = run_prompt(sample_prompt)
    print("Prompt:", sample_prompt)
    print("Response:", output)


if __name__ == "__main__":
    main()
