import requests

url = "http://localhost:8000/input_data/"

response = requests.post(url, json={"id":1, "name":"Apple", "price":5000})
print(response.status_code)
print(response.json())