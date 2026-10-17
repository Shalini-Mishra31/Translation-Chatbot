from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from typing import Literal, List
from PyPDF2 import PdfReader

class TranslationStates(BaseModel):
    inputFileType: str
    fileEmpty: bool
    fileContents: str
    translatedContents: str
    chatMessages: List[BaseMessage]
    endChat: bool

def getFile(State: TranslationStates):

    pdfPath = "C:\\Users\\Shalini_Mishra\\OneDrive - Dell Technologies\\Desktop\\Translation-chatbot\\ai\\langgraph\\utils\\kannada_text.pdf"
    reader = PdfReader(pdfPath)
    pages = reader.pages
    text = "\n".join(page.extract_text() or "" for page in pages)

    State.inputFileType = pdfPath[-3:]

    if(text == ""):
        State.fileEmpty = True
    else:
        State.fileEmpty = False

    State.fileContents = text

    return {
        "inputFileType": pdfPath.split(".")[-1],
        "fileEmpty": not bool(text.strip()),
        "fileContents": text
    }