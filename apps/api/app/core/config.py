from pydantic import BaseModel
import os
class Settings(BaseModel):
    database_url:str=os.getenv("DATABASE_URL","sqlite:///./smart_housing.db")
    ai_provider:str=os.getenv("AI_PROVIDER","ollama")
    ollama_base_url:str=os.getenv("OLLAMA_BASE_URL","http://localhost:11434")
settings=Settings()
