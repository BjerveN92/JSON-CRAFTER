from fastapi import APIRouter, HTTPException
from app.models.schemas import TransformRequest, TransformResponse
from app.services.codegen import get_generator

router = APIRouter()

SUPPORTED_LANGUAGES = {"java", "python", "typescript", "kotlin", "csharp", "go", "rust"}


@router.post("/transform", response_model=TransformResponse)
async def transform(request: TransformRequest):
    lang = request.language.lower()
    if lang not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Unsupported language: {lang}")

    generator = get_generator(lang)
    code = generator.generate(request.json_object, request.class_name)
    return TransformResponse(language=lang, code=code)
