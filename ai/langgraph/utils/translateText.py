from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from typing import Literal, List
from ai.LLMModel import mistralTranslationLLM

class TranslationStates(BaseModel):
    inputFileType: str
    fileEmpty: bool
    fileContents: str
    translatedContents: str
    chatMessages: List[BaseMessage]
    endChat: bool

from ai.LLMModel.mistralTranslationLLM import translationLLM

def translateText(State: TranslationStates):

    # State.translatedContents = translationLLM(State.fileContents)

    return {
        "translatedContents": translationLLM(State.fileContents)
    }
