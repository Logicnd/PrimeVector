# PrimeVector Architecture Overview

## Purpose

PrimeVector provides a modular base for AI-powered automation workflows with a mobile-first product mindset.

## Core Layers

1. **AI Core (`src/ai_core/`)**
   - Encapsulates model providers and prompt execution utilities.
   - Exposes `run_prompt(prompt: str) -> str` as the initial public API.

2. **Automations (`src/automations/`)**
   - Contains scripts/workflows that automate repetitive tasks.
   - Uses AI core helpers to reason, generate actions, or summarize outcomes.

3. **Utilities (`src/utils/`)**
   - Houses shared helpers (logging, config loading, file operations, etc.).

4. **Examples (`examples/`)**
   - Demonstrates runnable workflows and integration patterns.

5. **Tests (`tests/`)**
   - Will include unit tests for modules and integration tests for workflows.

## Initial Data Flow

1. User or trigger invokes an automation workflow.
2. Automation composes a prompt or retrieves template content.
3. AI core sends prompt to the model provider.
4. Workflow interprets output and executes follow-up action.
5. Result is logged or returned to caller.

## Mobile-First Considerations

- Keep workflows event-driven and concise for notification-style interactions.
- Build APIs that can be called by mobile apps or lightweight webhooks.
- Design response formats that are easy to render in compact interfaces.
