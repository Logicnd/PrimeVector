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

## HTTP API for Universal Clients

In addition to using PrimeVector as a library, you can run it as a web service. The repository provides a FastAPI wrapper under `src/primevector_api/app.py` that exposes a simple REST API.

### Running the API

First, ensure you have installed the additional dependencies listed in `requirements.txt` (`fastapi`, `uvicorn[standard]`, and `pydantic`). Then start the server with:

```bash
uvicorn primevector_api.app:app --host 0.0.0.0 --port 8000
```

The service will launch on port `8000` by default. You can change the host or port as needed.

### Endpoints

- **POST `/execute`** – Accepts a JSON payload with a `prompt` string and returns a JSON response containing the model’s output.

Example request:

```bash
curl -X POST http://localhost:8000/execute \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain the Prime Number Theorem."}'
```

Example response:

```json
{"response":"<model output here>"}
iOS

##### Integrating with iOS and other clients

Since the API is language‑agnostic, any client capable of making HTTP requests can interact with PrimeVector. On iOS, you can use `URLSession` to send requests and decode the JSON response. Here's a minimal example in Swift:

```swift
import Foundation

struct Prompt: Codable {
    let prompt: String
}

struct ResponseData: Codable {
    let response: String
}

func sendPrompt(_ text: String) {
    guard let url = URL(string: "https://your-backend-domain.com/execute") else { return }
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")

    let payload = Prompt(prompt: text)
    request.httpBody = try? JSONEncoder().encode(payload)

    URLSession.shared.dataTask(with: request) { data, _, error in
        guard let data = data, error == nil,
              let decoded = try? JSONDecoder().decode(ResponseData.self, from: data) else {
            print("Error:", error ?? NSError(domain: "com.primevector", code: -1, userInfo: nil))
            return
        }
        print("Model response:", decoded.response)
    }.resume()
}
```

This pattern can be adapted to any environment (e.g., a JavaScript frontend or another Python service) by issuing an HTTP POST request to the `/execute` endpoint.

## Contributing

We welcome contributions! Please review the [CONTRIBUTING.md](CONTRIBUTING.md) guide for instructions on how to set up your environment, adhere to our development practices, and submit pull requests. Bug reports, documentation improvements, and new features are all appreciated.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on GitHub or reach out to the maintainer at the email address listed in the project metadata.
