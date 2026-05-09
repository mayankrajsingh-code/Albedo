from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

response = client.chat.completions.create(
    model="qwen3.5-9b-glm5.1-distill-v1-i1",
    messages=[
        {
            "role": "user",
            "content": "Hello Albedo, who are you?"
        }
    ]
)

print(response.choices[0].message.content)