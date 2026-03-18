/**
 * Basic chat completion with CheapestInference using the OpenAI SDK.
 *
 * npm install openai
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.CHEAPEST_API_KEY,
  baseURL: "https://api.cheapestinference.com/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-chat",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What are the benefits of open-source LLMs?" },
  ],
  temperature: 0.7,
});

console.log(response.choices[0].message.content);
console.log(`\nTokens used: ${response.usage.total_tokens}`);
