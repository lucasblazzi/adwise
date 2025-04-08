from typing import List, TypedDict, Dict

from app.models.persona import Persona
from app.models.campaingn import Campaingn
from app.models.advertisement import Advertisement


class AgentState(TypedDict):
    persona: Persona
    campaign: Campaingn
    advertisement: Advertisement