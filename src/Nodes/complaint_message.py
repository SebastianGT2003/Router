from langgraph.types import Command, interrupt
from langgraph.graph import END, START, StateGraph
from agents import AGENT_REGISTRY
from utils.state import MessageState

def ComplaintMessage(state: MessageState)-> MessageState:
    """
    Classifies the intent of a message and provides a reason for the classification.

    Args:
        state (MessageState): The current state containing the message to classify.
    """
    #Traer el prompt de clasificación

    message= state.message
    case_id= state.case_id

    if not message:
        raise ValueError("El mensaje no puede estar vacío.")
    result = AGENT_REGISTRY["message_complaint"].invoke({"message": message, "case_id": case_id})
    return {"response": result.response}