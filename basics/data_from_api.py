#write a Python function that retrieves data from a public API (e.g., https://jsonplaceholder.typicode.com/posts) and returns the titles of the posts.

import requests
data_dict = []
def get_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data_dict = response.json()
    
    for i in data_dict:
        print(i["title"])

get_data()