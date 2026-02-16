"""Core AI module for loading OpenAI client and running prompts."""

from __future__ import annotations

import os

from openai import OpenAI


def _get_client() -> OpenAI:
    """Create and return an OpenAI client using environment configuration."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)


def run_prompt(prompt: str) -> str:
    """Run a prompt against a default model and return text output."""
    client = _get_client()
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )
    return response.output_text.strip()
