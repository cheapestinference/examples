"""Function/tool calling with CheapestInference.

Works with models that support tool use (DeepSeek, Qwen, Llama 3.3+).
"""

import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["CHEAPEST_API_KEY"],
    base_url="https://api.cheapestinference.com/v1",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name, e.g. 'San Francisco'",
                    }
                },
                "required": ["location"],
            },
        },
    }
]


def get_weather(location: str) -> str:
    """Fake weather function for demo purposes."""
    return json.dumps({"location": location, "temp_f": 72, "condition": "sunny"})


# First call: model decides to use the tool
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto",
)

message = response.choices[0].message

if message.tool_calls:
    tool_call = message.tool_calls[0]
    print(f"Model called: {tool_call.function.name}({tool_call.function.arguments})")

    # Execute the function
    result = get_weather(**json.loads(tool_call.function.arguments))

    # Second call: send the tool result back
    final = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": "What's the weather in Tokyo?"},
            message,
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            },
        ],
    )
    print(final.choices[0].message.content)
else:
    print(message.content)
