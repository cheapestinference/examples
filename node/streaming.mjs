/**
 * Streaming chat completion with CheapestInference.
 *
 * npm install openai
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.CHEAPEST_API_KEY,
  baseURL: "https://api.cheapestinference.com/v1",
});

const stream = await client.chat.completions.create({
  model: "deepseek-chat",
  messages: [{ role: "user", content: "Write a haiku about AI inference." }],
  stream: true,
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) process.stdout.write(content);
}

console.log(); // newline at end
