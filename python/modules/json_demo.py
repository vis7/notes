import json

details = {
    'name': 'vis',
    'city': 'ahmedabad',
    'work': 'entrepreneur'
}

# export dictionary to json file
with open('details.json', 'w') as f:
    json.dump(details, f)

# importing details from json file
with open('details.json', 'r') as f:
    loaded_details = json.load(f)

print(loaded_details)

# python dictionary to json string
details_str = json.dumps(details)

print(details_str)
print(type(details_str))

# json string ot python dictionary
detail_back = json.loads(details_str)
print(detail_back)
print(type(detail_back))
