from langgraph.types import Command, interrupt
from langgraph.graph import END, START, StateGraph
from agents import AGENT_REGISTRY
from utils.state import MessageState

def OtherMessage(state: MessageState)-> MessageState:
    return {"response": f"Solo puedo ayudarte con temas de facturación, soporte técnico o quejas de TelcoNet. ¿En qué te puedo ayudar?"}