emails = """
1. Subject: Standup Call at 10 AM
2. Subject: Client Review due by 5 PM
3. Subject: Lunch with Sarah at noon
4. Subject: AWS Budget Warning – 80% usage
5. Subject: Dentist Appointment - 4 PM
"""

from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    emails:str
    results:str

llm = ChatOpenAI(model="gpt-4o", temperature=0)

def calendar_summary_agent(state:AgentState) -> AgentState:
    prompt=f"Summarize today's schedule based on these emails, listing time-sensitive items first and then other important notes. Be concise and use bullet points:\n{emails}"
    summary = llm.invoke(prompt).content
    return{"results": summary, "emails": state["emails"]}

builder = StateGraph(AgentState)
builder.add_node("calendar", calendar_summary_agent)
builder.set_entry_point("calendar")
builder.set_finish_point("calendar")

graph =builder.compile()
result = graph.invoke({"emails": emails})
print(result["results"])

