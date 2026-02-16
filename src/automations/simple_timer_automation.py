# Demonstrates a simple timed automation workflow with AI summary placeholders.

from __future__ import annotations

import time

from src.ai_core.openai_client import run_prompt


def run_timer_automation(delay_seconds: int = 3) -> str:
    """Wait for a short delay, then summarize the automation result with AI."""
    if delay_seconds < 0:
        raise ValueError("delay_seconds must be non-negative.")

    time.sleep(delay_seconds)

    # Placeholder: replace with real task output (e.g., fetched data, moved file, API status).
    task_result = f"Timer completed after {delay_seconds} seconds."

    summary_prompt = (
        "You are an automation assistant. Summarize this task result for a mobile notification: "
        f"{task_result}"
    )

    # Placeholder behavior: this can be replaced with fallback logic if API calls are disabled.
    return run_prompt(summary_prompt)


if __name__ == "__main__":
    print(run_timer_automation())
