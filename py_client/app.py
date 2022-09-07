import json
import requests 

URL = "http://127.0.0.1:8000/createcoder/"

# r = requests.get(url=URL)

# json_data=r.json()

# print(json_data)

# post the data from client

data={
    'name':'jack dorsey',
    'domain':'Twitter',
    'company':'Twitter.io',
    'salary':10000000,
}
# convert data into json 

json_data = json.dumps(data)

r = requests.post(url=URL,data=json_data)

data = r.json()
print(data)