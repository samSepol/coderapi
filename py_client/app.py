import requests 

URL = "http://127.0.0.1:8000/coders"

r = requests.get(url=URL)

json_data=r.json()

print(json_data)