import json 

# with open("data.json", "r") as file: 
#  d = json.load(file)

#print(d)

new_data = {1:2, "hi":"hello"}

with open("data.json","r") as file: 
    data = json.load(file)
    data.update(new_data)

with open("data.json", "w") as data_file:
    json.dump(data, data_file, indent=4) 

