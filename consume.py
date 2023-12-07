import requests

response = requests.get('http://127.0.0:8000/drinks')
print(response.json())