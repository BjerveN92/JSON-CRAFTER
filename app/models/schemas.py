from pydantic import BaseModel
from typing import Any


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    json_object: dict[str, Any]


class TransformRequest(BaseModel):
    json_object: dict[str, Any]
    language: str
    class_name: str = "Root"


class TransformResponse(BaseModel):
    language: str
    code: str
