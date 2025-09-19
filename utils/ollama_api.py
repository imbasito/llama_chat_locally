import requests
import time

OLLAMA_URL = "http://localhost:11434/api/chat"

def query_ollama(model: str, history: list, retries: int = 3, delay: int = 2):
    """
    Query Ollama with full conversation history.
    - model: model name (e.g. llama3.1:8b)
    - history: list of {"role": "user"/"assistant", "content": "..."}
    """
    payload = {
        "model": model,
        "messages": history,
        "stream": False
    }

    for attempt in range(retries):
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()

        content = data.get("message", {}).get("content", "").strip()
        if content:
            return content

        # If model is still loading, retry
        time.sleep(delay)

    return "⚠️ Model loaded but returned no content. Try again."
