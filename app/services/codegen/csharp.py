from typing import Any
from .base import BaseGenerator


class CSharpGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "bool",
        "integer": "int",
        "float": "double",
        "string": "string",
        "array": "List<object>",
        "object": "Dictionary<string, object>",
        "unknown": "object",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        lines = [f"public class {class_name}", "{"]
        for name, value in json_object.items():
            t = self._TYPE_MAP[self._infer_type(value)]
            prop = name[0].upper() + name[1:]
            lines.append(f"    public {t} {prop} {{ get; set; }}")
        lines.append("}")
        return "\n".join(lines)
