from .tecnical_agent import TechnicalAgent
from .bills_agent import BillsAgent
from .classification_message_agent import ClassificationMessageAgent
from .complaint_message import ComplaintAgent


AGENT_REGISTRY= {
    "message_categorizer": ClassificationMessageAgent(),
    "message_billing": BillsAgent(),
    "message_technical": TechnicalAgent(),
    "message_complaint": ComplaintAgent()
}