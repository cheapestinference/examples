"""Basic chat completion with CheapestInference using the OpenAI SDK."""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["CHEAPEST_API_KEY"],
    base_url="https://api.cheapestinference.com/v1",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the benefits of open-source LLMs?"},
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)
print(f"\nTokens used: {response.usage.total_tokens}")
