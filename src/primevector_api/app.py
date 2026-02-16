"""FastAPI wrapper for PrimeVector."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from primevector.ai_core.client import OpenAIClient

app = FastAPI(title="PrimeVector API")

client = OpenAIClient.from_env()

class Prompt(BaseModel):
    prompt: str

@app.post("/execute")
async def execute(prompt_data: Prompt):
    """
    Execute a prompt using the PrimeVector OpenAI client.
    Example payload: { "prompt": "Hello world" }
    Returns JSON: { "response": "<model response>" }
    """
    try:
        result = client.execute(prompt_data.prompt)
        return {"response": result}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
