from typing import Any
from .base import BaseGenerator


class KotlinGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "Boolean",
        "integer": "Int",
        "float": "Double",
        "string": "String",
        "array": "List<Any>",
        "object": "Map<String, Any>",
        "unknown": "Any",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        fields = []
        for name, value in json_object.items():
            t = self._TYPE_MAP[self._infer_type(value)]
            fields.append(f"    val {name}: {t}")
        body = ",\n".join(fields)
        return f"data class {class_name}(\n{body}\n)"
