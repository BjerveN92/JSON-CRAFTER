from .base import BaseGenerator
from .java import JavaGenerator
from .python import PythonGenerator
from .typescript import TypeScriptGenerator
from .kotlin import KotlinGenerator
from .csharp import CSharpGenerator
from .go import GoGenerator
from .rust import RustGenerator

_GENERATORS: dict[str, BaseGenerator] = {
    "java": JavaGenerator(),
    "python": PythonGenerator(),
    "typescript": TypeScriptGenerator(),
    "kotlin": KotlinGenerator(),
    "csharp": CSharpGenerator(),
    "go": GoGenerator(),
    "rust": RustGenerator(),
}


def get_generator(language: str) -> BaseGenerator:
    return _GENERATORS[language]
