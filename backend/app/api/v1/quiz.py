from fastapi import APIRouter, status

from app.schemas.quiz_request import QuizGenerateRequest, QuizConfig
from app.schemas.quiz_response import QuizResponse
from app.schemas.question import Questions
from app.manager.quiz import get_quiz
from app.prompts.quiz import quiz_prompt

router = APIRouter(prefix="/quiz", tags=["Quiz"])


@router.post(
    path="/",
    # response_model=Questions,
    status_code=status.HTTP_200_OK,
    summary="Generate Quiz",
    description="Generate quiz based on provided text, URL or topic.",
)
def generate_quiz(request: QuizGenerateRequest):
    if request.text is not None:
        return quiz_from_text(request.text, request.config)


def quiz_from_text(text: str, config: QuizConfig) -> Questions:
    return get_quiz(messages=quiz_prompt(content=text))
