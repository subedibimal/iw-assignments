import json


print(dir(json))

print(help(json))

my_info = {"name": "Bimal Subedi", "age": 20}

json_str = json.dumps(my_info)
des_my_info = json.loads(json_str)

print(f"JSON: {json_str}")
