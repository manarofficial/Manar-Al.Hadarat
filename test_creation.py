import requests

url = "http://localhost:8000/token"
data = {"username": "admin", "password": "admin123", "grant_type": "password"}
response = requests.post(url, data=data)
token = response.json()["access_token"]

url = "http://localhost:8000/requests"
headers = {"Authorization": f"Bearer {token}"}
files = {'image': ('test.png', b'fakeimagebytes', 'image/png')}
data = {
    "product_name": "Test Product",
    "quantity": 1,
    "requester_name": "Test User"
}

response = requests.post(url, headers=headers, data=data, files=files)
print(response.status_code)
print(response.json())
