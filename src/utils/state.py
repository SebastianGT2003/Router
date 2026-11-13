from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

class MessageClassification(BaseModel):
    intent: Literal["billing", "technical", "complaint", "other"] = Field(
        ..., description="The intent of the message."
    )
    reason: str = Field(..., description="The reason for the intent classification.")

class MessageState(BaseModel):
    """
    Represents a message with its relevant details.
    """
    message: str = Field(..., description="The content of the email.")
    intent: str = Field(..., description="The intent of the email, e.g., 'billing', 'technical', etc.")
    reason: str = Field(..., description="The reason for the intent classification.")
    response: str = Field(..., description="The response generated for the email.")

    #Classification result
    classification: MessageClassification | None = None

    #Billing node specific fields
    bill_number: str | None = Field(None, description="The billing number associated with the message, if applicable.")
    date: datetime | None = Field(None, description="The date associated with the billing information, if applicable.")



