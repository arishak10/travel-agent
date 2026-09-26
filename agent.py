import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

print("ENV PATH:", ENV_FILE)
print("ENV EXISTS:", ENV_FILE.exists())
print("GROQ KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.8-27b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )