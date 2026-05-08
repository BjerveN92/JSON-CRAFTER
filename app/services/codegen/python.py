from typing import Any
from .base import BaseGenerator


class PythonGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "bool",
        "integer": "int",
        "float": "float",
        "string": "str",
        "array": "list",
        "object": "dict",
        "unknown": "Any",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        lines = ["from dataclasses import dataclass", "from typing import Any", "", "@dataclass", f"class {class_name}:"]

        for name, value in json_object.items():
            t = self._TYPE_MAP[self._infer_type(value)]
            lines.append(f"    {name}: {t}")

        return "\n".join(lines)
