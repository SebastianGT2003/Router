from .bills_message import BillsMessage
from .classification_message import ClassificationMessage
from .technical_message import TechnicalMessage
from .complaint_message import ComplaintMessage
from .other_message import OtherMessage

NODES= {
    "classification_message": ClassificationMessage,
    "bills_message": BillsMessage,
    "technical_message": TechnicalMessage,
    "complaint_message": ComplaintMessage,
    "other_message": OtherMessage
}