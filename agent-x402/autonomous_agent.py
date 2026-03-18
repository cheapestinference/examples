"""Autonomous agent that discovers CheapestInference, subscribes via x402, and runs.

This example shows how an AI agent can:
1. Discover the API via the A2A agent card
2. Receive a 402 with the product catalog
3. Subscribe with USDC on Base L2
4. Use the received API key for inference

Requirements:
    pip install openai httpx web3

Note: This is a reference implementation. The USDC payment step requires
a funded wallet on Base L2. See https://docs.cheapestinference.com/guides/x402/
"""

import httpx
from openai import OpenAI

API = "https://api.cheapestinference.com"


def discover_api():
    """Step 1: Discover the API via A2A agent card."""
    r = httpx.get(f"{API}/.well-known/agent.json")
    card = r.json()
    print(f"Discovered: {card['name']}")
    print(f"Skills: {[s['id'] for s in card.get('skills', [])]}")
    return card


def get_product_catalog():
    """Step 2: Send a request without a key to get the 402 product catalog."""
    r = httpx.post(
        f"{API}/v1/chat/completions",
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": "hi"}]},
    )

    if r.status_code != 402:
        raise RuntimeError(f"Expected 402, got {r.status_code}")

    data = r.json()
    products = data["x402"]["accepts"][0]["extra"]["products"]
    print(f"\nAvailable products:")
    for p in products:
        print(f"  - {p['type']}: {p.get('plan', 'credits')} ${p.get('price', p.get('minAmount'))}")
    return data


def subscribe_with_usdc(plan: str = "standard"):
    """Step 3: Subscribe by paying USDC on Base.

    In production, the agent would:
    1. Call /api/billing/checkout to get the payment address
    2. Send USDC via a web3 transaction on Base L2
    3. Call /api/billing/verify-usdc with the tx hash
    4. Receive an API key

    This step requires a funded wallet. See the x402 docs for details.
    """
    # 1. Get payment details
    # r = httpx.post(f"{API}/api/billing/checkout", json={"planSlug": plan, "method": "usdc"})
    # checkout = r.json()  # { address: "0x...", amount: "20" }

    # 2. Send USDC on Base (requires web3 + funded wallet)
    # tx_hash = send_usdc(checkout["address"], checkout["amount"])

    # 3. Verify payment and get API key
    # r = httpx.post(f"{API}/api/billing/verify-usdc", json={"txHash": tx_hash, "planSlug": plan})
    # return r.json()["apiKey"]

    raise NotImplementedError(
        "USDC payment requires a funded wallet on Base L2. "
        "See https://docs.cheapestinference.com/guides/x402/"
    )


def run_inference(api_key: str):
    """Step 4: Use the API key for inference."""
    client = OpenAI(
        api_key=api_key,
        base_url=f"{API}/v1",
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "What is x402?"}],
    )

    print(f"\nResponse: {response.choices[0].message.content}")
    return response


if __name__ == "__main__":
    # Demo: discovery and catalog (works without a wallet)
    card = discover_api()
    catalog = get_product_catalog()

    # To complete the flow with a real wallet:
    # api_key = subscribe_with_usdc("standard")
    # run_inference(api_key)
