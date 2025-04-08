from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from app.nodes import Node
from app.config import logger
from app.models.advertisement import Advertisement
from app.models.state import AgentState


class AdvertisementNode(Node):

    @staticmethod
    def map_language(language: str) -> str:
        language_map = {
            "en": "English",
            "pt": "Portuguese (Brazil)",
        }
        return language_map.get(language, language)

    def __call__(self, state: AgentState) -> dict:
        logger.info("[Advertisement Node] Generating advertisement...")
        llm = self.get_llm(model="gpt-4o-mini", temperature=0.7, top_p=0.9)

        language = self.map_language(state["campaign"]["language"])
        objective = state["campaign"]["objective"]
        client = self.format_prompt_input(state["campaign"]["client"])
        product = self.format_prompt_input(state["campaign"]["product"])
        company = self.format_prompt_input(state["campaign"]["company"])
        behavioral_insights = self.format_prompt_input(state["persona"]["behavioral_insights"])
        background = self.format_prompt_input(state["persona"]["background"])
        message_recommendation = self.format_prompt_input(state["persona"]["message_recommendation"])

        text_prompt = self.get_text_prompt(name="advertisement")
        system_prompt = self.get_text_prompt(name="system")

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", text_prompt),
                # MessagesPlaceholder(variable_name="history")
            ]
        )
        structured_llm = llm.with_structured_output(schema=Advertisement)
        prompt = prompt_template.invoke({
            "objective": objective,
            "client": client, 
            "product": product,
            "company": company,
            "behavioral_insights": behavioral_insights,
            "background": background,
            "message_recommendation": message_recommendation,
            "language": language
        })

        result = structured_llm.invoke(prompt)

        logger.info("[Advertisement Node] Advertisement generated successfully.")
        return {"advertisement": result}
