from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate

from app.nodes import Node
from app.state import AgentState 



class EntityNode(Node):

    def __call__(self, state: AgentState) -> dict:
        llm = self.get_llm(model="gpt-4o-mini", temperature=0)
        text_prompt = self.get_text_prompt(name="entity")

        prompt = PromptTemplate(
            input_variables=["text"],
            template=text_prompt
        )

        message = HumanMessage(content=prompt.format(text=state["text"]))
        entities = llm.invoke([message]).content.strip().split(", ")

        return {"entities": entities}