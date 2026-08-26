#JSON FILE HANDLING

# Converting Python Objects to JSON (Serialization)
# json.dumps() – Convert Python object to JSON string

import json


data = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(data)
print(json_string) 
print(type(json_string)) 

# Converting JSON to Python Objects (Deserialization)
# json.loads() – Convert JSON string to Python object

json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
python_obj = json.loads(json_data)
print(python_obj) 
print(type(python_obj))

# json.load() – Read JSON data from a file

with open("data.json","r") as file:
    data = json.load(file)

print(data)


# json.dump() – Write JSON data to a file

data = {
    "Name" : "OM",
     "Age" : 23,
     "Skills" : ["Python","SQL","ML","java"]   
}

with open("data.json","w") as file:
    json.dump(data,file,indent=4)

    print(data)