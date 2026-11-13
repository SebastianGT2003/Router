from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

class MessageClassification(BaseModel):
    intent: Literal["billing", "technical", "complaint", "other"] = Field(
        ..., description="The intent of the message."
    )
    reason: str = Field("", description="The reason for the intent classification.")

class BillingInfo(BaseModel):
    bill_number: str | None = Field(None, description="Número de factura mencionado en el mensaje, si existe.")
    date: str | None = Field(None, description="Fecha de la factura mencionada, si existe.")
    reason: str = Field("", description="Motivo del reclamo de facturación.")

class MessageState(BaseModel):
    """
    Represents a message with its relevant details.
    """
    message: str = Field(..., description="The content of the email.")
    intent: str = Field("", description="The intent of the email, e.g., 'billing', 'technical', etc.")
    reason: str = Field("", description="The reason for the intent classification.")
    response: str = Field("", description="The response generated for the email.")

    #Classification result
    classification: MessageClassification | None = None
    billing_info: BillingInfo | None = None  # Optional billing information


