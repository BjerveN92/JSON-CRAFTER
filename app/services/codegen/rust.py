from typing import Any
from .base import BaseGenerator


class RustGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "bool",
        "integer": "i64",
        "float": "f64",
        "string": "String",
        "array": "Vec<serde_json::Value>",
        "object": "std::collections::HashMap<String, serde_json::Value>",
        "unknown": "serde_json::Value",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        lines = [
            "#[derive(Debug, Serialize, Deserialize)]",
            f"pub struct {class_name} {{",
        ]
        for name, value in json_object.items():
            t = self._TYPE_MAP[self._infer_type(value)]
            lines.append(f"    pub {name}: {t},")
        lines.append("}")
        return "\n".join(lines)
