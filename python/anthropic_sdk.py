"""Using the Anthropic SDK with CheapestInference.

Any model available on CheapestInference works through the Anthropic endpoint.
"""

import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ["CHEAPEST_API_KEY"],
    base_url="https://api.cheapestinference.com/anthropic",
)

message = client.messages.create(
    model="deepseek-chat",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain quantum computing in 3 sentences."}],
)

print(message.content[0].text)
