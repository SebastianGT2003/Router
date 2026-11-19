from typing import Literal

from langgraph.graph import END
from langgraph.types import Command
from uuid_utils import uuid4

from agents import AGENT_REGISTRY
from utils.state import MessageState


def ClassificationMessage(state: MessageState) -> Command[Literal["bills_message", "technical_message","complaint_message", "other_message"]]:
    """
    Classifies the intent of a message and routes it to the right node.

    Args:
        state (MessageState): The current state containing the message to classify.
    """
    case_id = state.case_id or f"CASE-{uuid4().hex[:8].upper()}"
    message = state.message

    if not message:
        raise ValueError("El mensaje no puede estar vacío.")

    result = AGENT_REGISTRY["message_categorizer"].invoke({"message": message})

    if result.intent == "billing":
        # Si la intención es un problema de facturación, ir al nodo de facturación
        next_node = "bills_message"
    elif result.intent == "technical":
        # Si la intención es un problema de tecnología, ir al nodo de tecnología
        next_node = "technical_message"
    elif result.intent == "complaint":
        # Si la intención es una queja, ir al nodo de quejas
        next_node = "complaint_message"
    else:
        # De momento, las demás intenciones terminan el flujo
        next_node = "other_message"

    return Command(
        update={"classification": result, "case_id": case_id},
        goto=next_node,
    )
