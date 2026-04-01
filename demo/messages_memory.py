# how memory works in messages by appending to the messages list

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": "What is the capital of France?"
    },
    {
        "role":"system",
        "content":"you are a helpful research assistant"
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

reply = response.choices[0].message.content
print(f"Turn 1: {reply}")

# Now we append the new user message to the messages list, which allows the model to have context of the previous conversation
messages.append({"role":"assistant","content":reply}) # Append the assistant's reply to the messages list
# Now we can ask a follow-up question that relies on the previous context
messages.append({
    "role": "user",
    "content": "What is its population?"
})

#second api call 
response2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
reply2 = response2.choices[0].message.content
print(f"Turn 2: {reply2}")

print("\nFull conversation history:")
for m in messages:
    print(f"{m['role']}: {m['content']}")

# output: with memory
'''
Turn 1: The capital of France is Paris.
Turn 2: As of the last census data, the population of Paris is approximately 2.1 million people within its city limits. However, the wider metropolitan area, known as Île-de-France, has a population of over 12 million. Please note that population figures can vary over time, so it’s a good idea to consult the latest statistics for the most current numbers.

Full conversation history:
user: What is the capital of France?
system: you are a helpful research assistant
assistant: The capital of France is Paris.
user: What is the population of Paris?
'''

