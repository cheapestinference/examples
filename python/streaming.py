"""Streaming chat completion with CheapestInference."""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["CHEAPEST_API_KEY"],
    base_url="https://api.cheapestinference.com/v1",
)

stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Write a haiku about AI inference."}],
    stream=True,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)

print()  # newline at end
