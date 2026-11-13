from .bills_agent import BillsAgent
from .classification_message_agent import ClassificationMessageAgent


AGENT_REGISTRY= {
    "message_categorizer": ClassificationMessageAgent(),
    "message_billing": BillsAgent()
}