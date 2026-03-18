# CheapestInference Examples

Code examples for [CheapestInference](https://cheapestinference.com) — a flat-rate LLM inference API. No per-token billing.

## What is CheapestInference?

One API for every open-source model (DeepSeek, Qwen, Llama, Kimi, Gemma). Fixed monthly price. Uses the standard OpenAI and Anthropic SDKs — just change the base URL. Pay with card or USDC on Base L2.

See [current plans and pricing](https://cheapestinference.com/pricing).

## Quick start

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.cheapestinference.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Node.js

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://api.cheapestinference.com/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-chat",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(response.choices[0].message.content);
```

### cURL

```bash
curl https://api.cheapestinference.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-chat", "messages": [{"role": "user", "content": "Hello!"}]}'
```

## Examples

| Example | Description |
|---------|-------------|
| [python/chat.py](python/chat.py) | Basic chat completion |
| [python/streaming.py](python/streaming.py) | Streaming responses with SSE |
| [python/anthropic_sdk.py](python/anthropic_sdk.py) | Using the Anthropic SDK |
| [python/tool_calling.py](python/tool_calling.py) | Function/tool calling |
| [node/chat.mjs](node/chat.mjs) | Basic chat completion (Node.js) |
| [node/streaming.mjs](node/streaming.mjs) | Streaming responses (Node.js) |
| [agent-x402/autonomous_agent.py](agent-x402/autonomous_agent.py) | Agent that self-subscribes via x402 + USDC |

## x402: Agents that pay for themselves

CheapestInference supports the [x402 protocol](https://www.x402.org). AI agents can discover the API, subscribe with USDC on Base, and start making requests — no human setup:

```
Agent → GET /v1/chat/completions (no key)
     ← 402 Payment Required + product catalog
Agent → POST /api/billing/checkout (selects plan, pays USDC)
     ← { apiKey: "sk-..." }
Agent → GET /v1/chat/completions (with key)
     ← 200 OK
```

See the [full x402 example](agent-x402/autonomous_agent.py).

## Supported endpoints

| Endpoint | Description |
|----------|-------------|
| `POST /v1/chat/completions` | OpenAI-compatible chat |
| `POST /anthropic/v1/messages` | Anthropic-compatible messages |
| `POST /v1/embeddings` | Text embeddings |
| `GET /v1/models` | List available models |

## Links

- [Dashboard](https://cheapestinference.com) — Sign up, manage keys, view usage
- [Docs](https://docs.cheapestinference.com) — Full API reference
- [Pricing](https://cheapestinference.com/pricing) — All models with per-token costs and request estimates
