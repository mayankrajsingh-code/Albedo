from openai import OpenAI

# Connect Python to your local LM Studio server
client = OpenAI(
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1"
)

# Temporary conversation memory
conversation = []

# Infinite chat loop
while True:

    # Take user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Albedo: See you soon!")
        break

    # Store user message in memory
    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send full conversation to AI
    response = client.chat.completions.create(
        model="qwen3.5-9b-glm5.1-distill-v1-i1",
        messages=conversation
    )

    # Extract AI response text
    ai_reply = response.choices[0].message.content

    # Print AI response
    print("Albedo:", ai_reply)

    # Store AI response in memory
    conversation.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )