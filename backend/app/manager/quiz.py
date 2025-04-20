from app.services.llm import llm
from app.schemas.question import Questions

structured_llm = llm.with_structured_output(Questions)


def get_quiz(messages) -> Questions:
    ai_quiz = structured_llm.invoke(messages)
    return ai_quiz
