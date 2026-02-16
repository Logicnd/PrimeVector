# PrimeVector

## Overview

PrimeVector is a Python‑based framework for orchestrating and running AI models with a consistent interface. It provides modules to manage configuration, wrap around the OpenAI API, automate tasks, and demonstrate use‑cases through example scripts. The goal is to accelerate development of intelligent systems by providing scaffolding for experimentation and deployment.

## Features

- **Model Runner**: Execute prompts against OpenAI models with standardized client wrapper and error handling.
- **Configuration Management**: Load model and project settings from environment variables and `.env` files.
- **Automation Scripts**: Automate common tasks, such as batch inference or data processing, using simple CLI commands.
- **Example Projects**: Contains example pipelines demonstrating how to leverage PrimeVector components.
- **Utility Helpers**: Common utility functions for logging, text manipulation, and API integration.

## Installation

Follow these steps to install PrimeVector and its dependencies:

1. Ensure you have Python 3.9+ installed.
2. Clone the repository:

   ```bash
   git clone https://github.com/Logicnd/PrimeVector.git
   cd PrimeVector
   ```

3. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

PrimeVector includes a client wrapper for the OpenAI API and example scripts. Here is a simple example showing how to run a prompt using the library:

```python
from primevector.ai_core.client import OpenAIClient

client = OpenAIClient.from_env()  # loads API key and defaults from .env

prompt = "Explain the Prime Number Theorem."
response = client.execute(prompt)
print(response)
```

You can also explore the `examples/` and `scripts/` directories for more advanced use cases and automation scripts.

## Project Structure

- `primevector/ai_core/` – Core modules for model interaction and configuration.
- `primevector/utils/` – Helper functions and utilities.
- `examples/` – Sample notebooks and scripts demonstrating framework usage.
- `scripts/` – Command‑line tools for automation.
- `tests/` – Unit tests for ensuring reliability.

## Contributing

We welcome contributions! Please review the [CONTRIBUTING.md](CONTRIBUTING.md) guide for instructions on how to set up your environment, adhere to our development practices, and submit pull requests. Bug reports, documentation improvements, and new features are all appreciated.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on GitHub or reach out to the maintainer at the email address listed in the project metadata.
