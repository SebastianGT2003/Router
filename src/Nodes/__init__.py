from .bills_message import BillsMessage
from .classification_message import ClassificationMessage
from .technical_message import TechnicalMessage


NODES= {
    "classification_message": ClassificationMessage,
    "bills_message": BillsMessage,
    "technical_message": TechnicalMessage
}