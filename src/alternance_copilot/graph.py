from langgraph.graph import END, START, StateGraph

from alternance_copilot.agents.offer_analyzer import analyze_offer
from alternance_copilot.state import State


builder = StateGraph(State)

builder.add_node("offer_analyzer", analyze_offer)
builder.add_edge(START, "offer_analyzer")
builder.add_edge("offer_analyzer", END)

graph = builder.compile()