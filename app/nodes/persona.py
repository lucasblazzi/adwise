from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.nodes import Node
from app.config import logger
from app.models.persona import Persona
from app.models.state import AgentState


# Command Pattern
class PersonaNode(Node):

    def __call__(self, state: AgentState) -> dict:
        logger.info("[Persona Node] Generating persona...")
        llm = self.get_llm(model="gpt-4o-mini", temperature=0.7, top_p=0.9)

        client = self.format_prompt_input(state["campaign"]["client"])
        product = self.format_prompt_input(state["campaign"]["product"])

        text_prompt = self.get_text_prompt(name="persona")
        system_prompt = self.get_text_prompt(name="system")

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", text_prompt),
                # MessagesPlaceholder(variable_name="history")
            ]
        )
        structured_llm = llm.with_structured_output(schema=Persona)
        prompt = prompt_template.invoke({"client": client, "product": product})

        result = structured_llm.invoke(prompt)
        logger.info("[Persona Node] Persona generated successfully.")
        return {"persona": result}
