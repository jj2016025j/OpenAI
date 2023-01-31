import openai
#API Key
openai.api_key = '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'

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="講個笑話來聽聽",
    max_tokens=128,
    temperature=0.5,
)

completed_text = response["choices"][0]["text"]
print(completed_text)