from fastapi import FastAPI

from app.api.v1.quiz import router


app = FastAPI(
    title="Quiz Generator API",
    description="API to generaye quizzes from text, URL, file or topic",
    version="1.0.0",
)

app.include_router(router=router)
