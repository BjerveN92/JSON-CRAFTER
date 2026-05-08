from typing import Any
from .base import BaseGenerator


class GoGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "bool",
        "integer": "int",
        "float": "float64",
        "string": "string",
        "array": "[]interface{}",
        "object": "map[string]interface{}",
        "unknown": "interface{}",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        lines = [f"type {class_name} struct {{"]
        for name, value in json_object.items():
            t = self._TYPE_MAP[self._infer_type(value)]
            exported = name[0].upper() + name[1:]
            lines.append(f'    {exported} {t} `json:"{name}"`')
        lines.append("}")
        return "\n".join(lines)
