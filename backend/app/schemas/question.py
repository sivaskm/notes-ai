from pydantic import BaseModel, Field
from typing import Optional, Literal, List

class QuestionOption(BaseModel):
    option_id: str = Field(..., description="Unique identifier for the option. Goes like a, b, c etc.,")
    text: str = Field(..., description="Text content of the option.")

class Question(BaseModel):
    question_id: str = Field(..., description="Unique identifier for the question starting from 1.")
    text: str = Field(..., description="The actual text of the question.")
    type: Literal["mcq", "msq"] = Field(..., description="Type of the question. Can be 'mcq' or 'msq'.")
    options: Optional[List[QuestionOption]] = Field(..., description="List of possible options.")
    correct_option_ids: list[str] = Field(..., description="Correct options' IDs. Single value for MCQ and multiple values from MSQs. Goes like a, b, c etc.,")
    correct_answer: List[str] = Field(..., description="List of correct answer(s). For MCQ it typically has one value; for MSQ, it can have multiple acceptable answers.")
    explanation: Optional[str] = Field(..., description="Short explanation for the answer. Do not quote from the given content. Give general explanation. Even if you take it from the given content, do not reveal to the user.")

class Questions(BaseModel):
    questions: list[Question] = Field(..., description="List of questions")
