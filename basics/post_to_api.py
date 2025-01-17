#Write a Python script that makes a POST request to a REST API.

import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "Suresh Joshi",
    "job": "Software Engineer"
}
response = requests.post(url, json=payload)

print("Response Code:", response.status_code)
print("Response Body:", response.json())

