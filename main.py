import os
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
    )
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(model="llama3",temperature=0)


# --- DEFINE OUTPUT DATA ---
class Players(BaseModel):
    # The `values` field in the `Players` class is a list that contains information about players,
    # including their name and nationality. It is used to store the list of players retrieved from the
    # model's response.
    values : list = Field(description="List of players with name and nationality")
    city : str = Field(description="Give me the most popular country across the results")
    
parser = PydanticOutputParser(pydantic_object=Players)

print(parser.get_format_instructions())

# --- DEFINE PROMPT ---
human_prompt = HumanMessagePromptTemplate.from_template("{request}\n{format_instructions}") 
chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

request = chat_prompt.format_prompt(
    request="Give me the top 10 players in the world",
    format_instructions=parser.get_format_instructions()
).to_messages()

# --- CALL MODEL ---
response = model.invoke(request)

# --- PARSE RESPONSE ---
parsed_response = parser.parse(response.content) # Player class object
print(f'results_values = {parsed_response}, {type(parsed_response)}')


import pandas as pd

results_dataframe = pd.DataFrame.from_dict(parsed_response.values)

print(results_dataframe.head(10));
print(results_dataframe.shape);

print(f'The most popular city across the results is {parsed_response.city}')