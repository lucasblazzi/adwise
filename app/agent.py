from langgraph.graph import StateGraph, END

from app.models.state import AgentState
from app.nodes.persona import PersonaNode
from app.nodes.advertisement import AdvertisementNode


workflow = StateGraph(AgentState)

workflow.add_node("persona_node", PersonaNode())
workflow.add_node("advertisement_node", AdvertisementNode())
workflow.set_entry_point("persona_node")
workflow.add_edge("persona_node", "advertisement_node")
workflow.add_edge("advertisement_node", END)

app = workflow.compile()


with open("C:/Users/User/Blazzi/Repositories/adwise/results/graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())