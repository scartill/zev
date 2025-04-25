from pydantic import BaseModel
from typing import Optional


class Command(BaseModel):
    command: str
    short_explanation: str


class OptionsResponse(BaseModel):
    commands: list[Command]
    is_valid: bool
    explanation_if_not_valid: Optional[str] = None
