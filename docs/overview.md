# PrimeVector Architecture Overview

## Purpose

PrimeVector provides a modular Python foundation for AI-driven automation workflows with a mobile-first product direction.

## High-Level Components

- **AI Core (`src/ai_core`)**
  - Handles model client setup and prompt execution.
  - Will evolve to include prompt templates, tool calling, and response guards.

- **Automations (`src/automations`)**
  - Contains individual automation scripts and workflow logic.
  - Current example shows a web fetch workflow stub.

- **Utilities (`src/utils`)**
  - Shared utilities such as config loading and environment helpers.

- **Examples (`examples`)**
  - Runnable scripts that demonstrate how developers can use project modules quickly.

- **Tests (`tests`)**
  - Placeholder test files defining what unit and integration tests should cover.

## Initial Execution Flow

1. A script or service receives a user task.
2. The task is transformed into a prompt.
3. `run_prompt` in `src/ai_core/model_runner.py` sends the prompt to OpenAI.
4. The response is returned to the calling automation.
5. Automation logic performs follow-up actions (fetch data, move files, schedule tasks, etc.).

## Future Extensions

- Mobile-facing API endpoints and webhook triggers.
- Persistent workflow definitions and job queue support.
- Better observability (structured logs, traces, run history).
