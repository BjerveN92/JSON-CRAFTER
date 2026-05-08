from abc import ABC, abstractmethod
from typing import Any


class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        ...

    def _infer_type(self, value: Any) -> str:
        if isinstance(value, bool):
            return "boolean"
        if isinstance(value, int):
            return "integer"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "string"
        if isinstance(value, list):
            return "array"
        if isinstance(value, dict):
            return "object"
        return "unknown"
