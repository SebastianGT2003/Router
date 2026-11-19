from langgraph.types import Command, interrupt
from langgraph.graph import END, START, StateGraph
from agents import AGENT_REGISTRY
from utils.state import MessageState

def TechnicalMessage(state: MessageState)-> MessageState:
    """
    Classifies the intent of a message and provides a reason for the classification.

    Args:
        state (MessageState): The current state containing the message to classify.
    """
    #Traer el prompt de clasificación

    message= state.message

    if not message:
        raise ValueError("El mensaje no puede estar vacío.")
    result = AGENT_REGISTRY["message_technical"].invoke({"message": message})
    return {"response": result.response}