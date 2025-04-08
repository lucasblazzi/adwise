from typing import List, TypedDict, Dict


class BehavioralInsights(TypedDict):
    spending_habits: List[str]
    interests: List[str]
    potential_motivations: List[str]
    potential_barriers: List[str]


class Background(TypedDict):
    daily_routine: List[str]
    hobbies: List[str]
    goals: List[str]


class MessageRecommendation(TypedDict):
    tone: str
    suggested_aproach: str
    communication_channel: str


class Persona(TypedDict):
    behavioral_insights: BehavioralInsights
    background: Background
    message_recommendation: MessageRecommendation
