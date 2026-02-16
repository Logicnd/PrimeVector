"""OpenAI client wrapper for PrimeVector.

Provides a small, stable interface (`run_prompt`) so the rest of the project does not
depend on the details of the OpenAI SDK.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from openai import OpenAI


@dataclass(frozen=True)
class AIConfig:
    """Runtime configuration for model execution."""
    model: str
    api_key: str | None = None


def load_config() -> AIConfig:
    """Load configuration from environment variables."""
    load_dotenv()
    model = os.getenv("PRIMEVECTOR_MODEL", "gpt-4o-mini")
    api_key = os.getenv("OPENAI_API_KEY")
    return AIConfig(model=model, api_key=api_key)


def run_prompt(prompt: str) -> str:
    """Run a user prompt against the configured OpenAI model.

    Args:
        prompt: The user prompt text.

    Returns:
        The model output text.

    Raises:
        ValueError: If the prompt is empty or only whitespace.
    """
    if not prompt or not prompt.strip():
        raise ValueError("Prompt must be a non-empty string.")

    cfg = load_config()
    client = OpenAI(api_key=cfg.api_key)

    response = client.responses.create(
        model=cfg.model,
        input=prompt,
    )

    return response.output_text.strip()
