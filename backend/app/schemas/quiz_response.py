from pydantic import BaseModel
from typing import Literal, Optional

from app.schemas.quiz_request import QuizConfig


class SourceInfo(BaseModel):
    type: Literal["text", "url", "topic", "file"]
    content: str


class QuestionOption(BaseModel):
    option_id: str
    text: str


class Question(BaseModel):
    question_id: str
    text: str
    type: Literal["mcq", "true_false", "short_answer"]
    options: Optional[list[QuestionOption]] = None
    correct_answer: list[str]
    explanation: Optional[str] = None


class QuizResponse(BaseModel):
    quiz_id: str
    title: str
    source: SourceInfo
    config: QuizConfig
    questions: list[Question]
