import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


llm = init_chat_model(
    model="gemini-2.5-flash-preview-04-17",
    model_provider="google_genai",
    temperature=0,
    api_key=os.getenv("GEMINI_API_KEY"),
)
