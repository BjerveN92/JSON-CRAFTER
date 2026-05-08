import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

_client = OpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)

MODEL = "accounts/fireworks/models/qwen3-235b-a22b"

SYSTEM_PROMPT = """You are a JSON generator. Given a description, respond with ONLY a valid JSON object — no explanation, no markdown, no code fences. The JSON should reflect a realistic data model for the described entity."""


async def generate_json(prompt: str) -> dict:
    response = _client.chat.completions.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    raw = response.choices[0].message.content.strip()
    return json.loads(raw)
