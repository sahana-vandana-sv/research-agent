#agent loop

from openai import OpenAI
from dotenv import load_dotenv
import sys
sys.path.append('../')  # Add the parent directory to the path
from mock_search_tool import mock_search

load_dotenv()
client = OpenAI()

MAX_ITERATIONS = 5
def log_iteration(i:int, decision:str,detail:str):
    print(f"\nIteration {i + 1}:")
    print(f"Decision: {decision}")
    print(f"Detail: {detail[:200]}")  # Print only the first 200 characters for brevity

def run_agent(question:str)->str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a research agent. "
                "When you have enough information to answer, "
                "say FINAL ANSWER: followed by your answer. "
                "If you need to search for information first, "
                "say SEARCH: followed by your search query."
            )
        },
        {"role": "user", "content": question}
    ]

    for i in range(MAX_ITERATIONS):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content.strip()
        print(f"Agent: {reply[:200]}")

        if "FINAL ANSWER" in reply:
            answer = reply.split("FINAL ANSWER:")[-1].strip()
            log_iteration(i, "Final Answer", answer)
            return answer
            
        elif "SEARCH:" in reply:
            search_query = reply.split("SEARCH:")[-1].strip()
            search_results = mock_search(search_query)
            log_iteration(i, "Search", f"Query: {search_query}\nResults: {search_results[:200]}")
            messages.append({"role": "assistant", "content": reply})
            messages.append({"role": "system", "content": search_results})

        else:
            print("⚠️ Agent response did not contain a valid action. Ending loop.")
            break
    return "Agent failed to provide a final answer within the iteration limit."

if __name__ == "__main__":
    question = "What are the effects of sleep deprivation on cognitive function?"
    answer = run_agent(question)
    print(f"Final answer:\n{answer}")

