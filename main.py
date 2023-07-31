from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

f = open("openai_api_key.txt", "r")
openai_api_key = f.read()

chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
out = chat(
    [
        SystemMessage(content="You are an unhelpful AI bot that makes a joke at whatever the user says"),
        HumanMessage(content="I would like to go to New York, how should I do this?")
    ]
)



print(out)