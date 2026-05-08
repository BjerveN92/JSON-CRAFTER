from typing import Any
from .base import BaseGenerator


class JavaGenerator(BaseGenerator):
    _TYPE_MAP = {
        "boolean": "boolean",
        "integer": "int",
        "float": "double",
        "string": "String",
        "array": "List<Object>",
        "object": "Object",
        "unknown": "Object",
    }

    def generate(self, json_object: dict[str, Any], class_name: str) -> str:
        lines = [f"public class {class_name} {{"]

        fields = {k: self._infer_type(v) for k, v in json_object.items()}

        for name, t in fields.items():
            java_type = self._TYPE_MAP[t]
            lines.append(f"    private {java_type} {name};")

        lines.append("")

        for name, t in fields.items():
            java_type = self._TYPE_MAP[t]
            cap = name[0].upper() + name[1:]
            lines.append(f"    public {java_type} get{cap}() {{ return {name}; }}")
            lines.append(f"    public void set{cap}({java_type} {name}) {{ this.{name} = {name}; }}")

        lines.append("}")
        return "\n".join(lines)
