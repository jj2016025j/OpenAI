import requests

url = "http://localhost:5000/message/"
data = {"message": "Hello, world!"}

response = requests.post(url, data=data)

url = "http://localhost:5000/message/Hello, world!"
response = requests.get(url)

print(response.text)
print(response)