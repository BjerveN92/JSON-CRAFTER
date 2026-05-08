from fastapi import APIRouter
from app.models.schemas import GenerateRequest, GenerateResponse
from app.services import llm

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    json_object = await llm.generate_json(request.prompt)
    return GenerateResponse(json_object=json_object)
