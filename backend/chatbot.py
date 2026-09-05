# https://www.freecodecamp.org/news/how-to-build-api-documentation-from-scratch-roadmap/

# Import libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from pathlib import Path
from dotenv import load_dotenv

# Find project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(BASE_DIR/".env")

# To ensure .env variables are loaded
# python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(bool(os.getenv('GROQ_API_KEY')))"

# Step 1: Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a very good AI assistant. Please respond to the user's query"),
    ("user", "question: {question}"),
])

# Step 2: LLM Model
llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0.01
)

# Step 3: Output Parser
output_parser = StrOutputParser()

# Step 4: Chain
chain = prompt | llm | output_parser

def get_response(question: str) -> str:
    response = chain.invoke({'question': question})
    return response

