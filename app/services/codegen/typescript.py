from typing import Any
from .base import BaseGenerator


class TypeScriptGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "boolean",
        "integer": "number",
        "float": "number",
        "string": "string",
        "array": "unknown[]",
        "object": "Record<string, unknown>",
        "unknown": "unknown",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        lines = [f"interface {class_name} {{"]
        for name, value in json_object.items():
            t = self._TYPE_MAP[self._infer_type(value)]
            lines.append(f"  {name}: {t};")
        lines.append("}")
        return "\n".join(lines)
