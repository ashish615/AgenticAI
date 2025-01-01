from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Write a love story between a tomato and a chili.',
  },
])
print(response['message']['content'])
print(response.message.content)
