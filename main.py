import os
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
    )
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(model="llama3")


# --- DEFINE OUTPUT DATA ---
class Players(BaseModel):
    values : list = Field(description="List of players with name and nationality")
    city : str = Field(description="Give me the most popular country across the results")
    
parser = PydanticOutputParser(pydantic_object=Players)

print(parser.get_format_instructions())
