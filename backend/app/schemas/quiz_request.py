from typing import Optional, Literal
from typing_extensions import Self
from pydantic import BaseModel, model_validator


DEFAULT_NUM_QUESTIONS = None
DEFAULT_DIFFICULTY = "medium"
DEFAULT_QUIZ_TYPE = "mcq"


class QuizConfig(BaseModel):
    num_questions: Optional[int] = DEFAULT_NUM_QUESTIONS
    difficulty: Optional[Literal["easy", "medium", "hard"]]
    quiz_type: Optional[Literal["mcq", "true_false", "short_answer"]]


class QuizGenerateRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None
    topic: Optional[str] = None
    config: QuizConfig

    @model_validator(mode="after")
    def check_one_source(self) -> Self:
        if not (self.text or self.url or self.topic):
            raise ValueError("Atleast one source should be given")
        return self
