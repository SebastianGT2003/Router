from typing import Literal

from langgraph.graph import END
from langgraph.types import Command

from agents import AGENT_REGISTRY
from utils.state import MessageState


def ClassificationMessage(state: MessageState) -> Command[Literal["bills_message", "__end__"]]:
    """
    Classifies the intent of a message and routes it to the right node.

    Args:
        state (MessageState): The current state containing the message to classify.
    """
    message = state.message

    if not message:
        raise ValueError("El mensaje no puede estar vacío.")

    result = AGENT_REGISTRY["message_categorizer"].invoke({"message": message})

    if result.intent == "billing":
        # Si la intención es un problema de facturación, ir al nodo de facturación
        next_node = "bills_message"
    else:
        # De momento, las demás intenciones terminan el flujo
        next_node = END

    return Command(
        update={"classification": result},
        goto=next_node,
    )
