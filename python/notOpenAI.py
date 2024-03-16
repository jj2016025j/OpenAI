# 非openAI的語言模型
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "你是一個主要說繁體中文的語音助理"},
    {"role": "user", "content": "跟我講一些關於llm的基礎知識"}
  ],
  temperature=1,
  max_tokens=100,
)

print(completion.choices[0].message.content)