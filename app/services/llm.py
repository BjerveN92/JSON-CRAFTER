import os
import re
import json
from openai import AsyncOpenAI
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

_client = AsyncOpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url=os.getenv("FIREWORKS_BASE_URL"),
)

MODEL = os.getenv("FIREWORKS_MODEL")

SYSTEM_PROMPT = """You are a JSON generator. Given a description,
                    respond with ONLY a valid JSON object — no explanation,
                    no markdown, no code fences. The JSON should reflect a
                    realistic data model for the described entity."""


def _extract_json(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```(?:json)?(.*?)```", r"\1", text, flags=re.DOTALL)
    return text.strip()


async def generate_json(prompt: str) -> dict:
    try:
        response = await _client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        )
        message = response.choices[0].message
        content = message.content or ""
        print(f"[llm] raw content: {repr(content[:500])}")
        raw = _extract_json(content)
        if not raw:
            raise HTTPException(status_code=422, detail=f"Modellen returnerade tomt svar. Raw: {repr(content[:200])}")
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=422, detail=f"Modellen returnerade ogiltig JSON: {e}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"LLM-fel: {e}")
