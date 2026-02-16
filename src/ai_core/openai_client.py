# Provides a minimal OpenAI client wrapper for prompt execution.

from __future__ import annotations

import os

from openai import OpenAI

DEFAULT_MODEL = "gpt-4o-mini"


def _get_client() -> OpenAI:
    """Create and return an initialized OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set. Please export it before calling run_prompt.")

    return OpenAI(api_key=api_key)


def run_prompt(prompt: str) -> str:
    """Run a prompt against the configured OpenAI model and return plain text output."""
    if not prompt.strip():
        raise ValueError("Prompt must not be empty.")

    client = _get_client()
    response = client.responses.create(
        model=DEFAULT_MODEL,
        input=prompt,
    )

    return response.output_text.strip()
