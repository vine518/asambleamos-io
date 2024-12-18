from fastapi import APIRouter

from app.ai.service.llm_adapter import ai_response_generator

messages_history = []

router = APIRouter()


# SSE endpoint
@router.get('/api/sse/{prompt}')
async def sse_ai_response(prompt: str):
    # Check if prompt is empty
    response = await ai_response_generator(prompt)
    return {"message": response}
