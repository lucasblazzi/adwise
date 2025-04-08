from langchain_openai import ChatOpenAI

from app.config import env
from app.models.state import AgentState


class Node:

    @staticmethod
    def get_text_prompt(name) -> str:
        with open(f"app/prompts/{name}.txt", "r", encoding="utf8") as file:
            prompt = file.read()
        return prompt
    
    @staticmethod
    def get_llm(**kwargs) -> ChatOpenAI:
        return ChatOpenAI(api_key=env.open_ai_api_key, **kwargs)

    @staticmethod
    def format_prompt_input(value):
        return "\n".join([
            f"{k.replace('_', ' ').title()}: {"\n- ".join(v) if isinstance(v, list) else v}" 
            for k, v in value.items()
        ])
    
    def __call__(self, state: AgentState) -> dict:
        raise NotImplementedError