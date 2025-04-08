from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from app.nodes import Node
from app.state import AgentState


class SummarizeNode(Node):

    def __call__(self, state: AgentState) -> dict:
        llm = self.get_llm(model="gpt-4o-mini", temperature=0)
        text_prompt = self.get_text_prompt(name="summarize")

        prompt = PromptTemplate.from_template(text_prompt)

        chain = prompt | llm
        response = chain.invoke({"text": state["text"]})
        
        return {"summary": response.content}
    