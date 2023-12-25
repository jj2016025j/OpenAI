from openai import OpenAI
import json
    
try:
    with open('config.json', 'r') as file:
        config = json.load(file)
except Exception as e:
    print(f"錯誤: {e}")

OPENAI_API_KEY = config["OPENAI_API_KEY"]

#=========================================================

# client = OpenAI(
#     api_key = OPENAI_API_KEY,
#     # organization='org-gHXvyBFxxwtSPuWwo1W6eGQ5',
# )
# stream = client.chat.completions.create(
#     model="gpt-4",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
# {
#   "id": "unique-chat-id",
#   "object": "chat_completion",
#   "created": 1234567890,
#   "model": "gpt-4",
#   "choices": [
#     {
#       "message": {
#         "role": "assistant",
#         "content": "This is a test."
#       },
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "stop"
#     }
#   ]
# }

#=========================================================

response = OpenAI.Completion.create(
    api_key = OPENAI_API_KEY,
    engine="text-davinci-003",
    prompt="翻译以下文本到英文：'你好，世界！'",
    max_tokens=1
)

print(response.choices[0].text.strip())
# {
#   "id": "unique-id",
#   "object": "text_completion",
#   "created": 1234567890,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "Hello, world!",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "length"
#     }
#   ]
# }

#=========================================================

# response = OpenAI.Completion.create(
#     openai.api_key = OPENAI_API_KEY
#     model="text-davinci-003",
#     prompt="講個笑話來聽聽",
#     max_tokens=1,
#     temperature=0.5,
# )

# completed_text = response["choices"][0]["text"]
# print(completed_text)

#=========================================================

# client = OpenAI(
#     api_key = OPENAI_API_KEY
# )

# completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-3.5-turbo",
# )

# for message in completion.choices[0].message:
#     if message['role'] == 'assistant':
#         print(f"{message['role']}: {message['content']}")
#輸出訊息
# ChatCompletion(
#     id='chatcmpl-8Zg07T00QWlwCJQljwMSk9EvTEwOq', 
#     choices=[
#         Choice(
#             finish_reason='stop', 
#             index=0, 
#             logprobs=None, 
#             message=ChatCompletionMessage(
#                 content='This is a test.', 
#                 role='assistant', 
#                 function_call=None, 
#                 tool_calls=None
#             )
#         )
#     ], 
#     created=1703513623, 
#     model='gpt-3.5-turbo-0613', 
#     object='chat.completion', 
#     system_fingerprint=None, 
#     usage=CompletionUsage(
#         completion_tokens=5, 
#         prompt_tokens=12, 
#         total_tokens=17
#     )
# )

#=========================================================

#2023/12/25還可以用
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message)
# ChatCompletionMessage(content='Hello! How can I assist you today?', role='assistant', function_call=None, tool_calls=None)