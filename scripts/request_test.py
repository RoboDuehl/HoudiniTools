import json 
import requests

URL = "https://jsonplaceholder.typicode.com/posts" 

response = requests.get(url=URL)

d = response.json()
print(d) 

# with open("data.json", "w") as file: 
#  json.dump(new_data, file, indent=4)

