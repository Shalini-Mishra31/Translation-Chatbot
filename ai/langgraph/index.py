from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from typing import Literal, List
from ai.langgraph.utils.getFile import getFile
from ai.langgraph.utils.translateText import translateText

class TranslationStates(BaseModel):
    inputFileType: str
    fileEmpty: bool
    fileContents: str
    translatedContents: str
    chatMessages: List[BaseMessage]
    endChat: bool

graph = StateGraph(TranslationStates)

graph.add_node('getFile',getFile)
graph.add_node('translateText',translateText)
graph.add_node('vectorize',vectorize)
graph.add_node('chatNode',chatNode)

graph.add_edge(START, 'getFile')
graph.add_edge('getFile', 'translateText')
graph.add_edge('translateText', 'vectorize')
graph.add_edge('vectorize', 'chatNode')


def routerNode(state: TranslationStates) -> Literal['chatNode','end']:
    if(state.endChat == True):
        return "end"
    else:
        return "chatNode"


graph.add_conditional_edges('chatNode',routerNode,{
    "chatNode": "chatNode",
    "end": END,
})

workflow = graph.compile()

initial_state = {
    'inputFileType': "pdf",
    'fileEmpty': False,
    'fileContents': "Mei hoon shalini mishra",
    'translatedContents': "I am shalini mishra",
    'chatMessages': [],
    'endChat': False,
}

output = workflow.invoke(initial_state)

print(output)