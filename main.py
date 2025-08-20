import os
from langchain.llms import Ollama
from langchain.chat_models import ChatOllama
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
    )
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(model="llama3")

