from openai import OpenAI
import json

# Connect Python to local LM Studio server
client = OpenAI(
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1"
)

# Memory file
MEMORY_FILE = "memory.json"
MAX_CONTEXT = 10

# Load previous memory
try:
    with open(MEMORY_FILE, "r") as file:
        conversation = json.load(file)

except FileNotFoundError:
    conversation = []

# Infinite chat loop
while True:

    # User input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Albedo: See you soon!")
        break

    # Store user message
    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate AI response
    response = client.chat.completions.create(
        model="qwen3.5-9b-glm5.1-distill-v1-i1",
        messages=conversation[-MAX_CONTEXT:]
    )

    # Extract AI text
    ai_reply = response.choices[0].message.content

    # Print response
    print("Albedo:", ai_reply)

    # Store AI response
    conversation.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    # Save memory
    with open(MEMORY_FILE, "w") as file:
        json.dump(conversation, file, indent=4)