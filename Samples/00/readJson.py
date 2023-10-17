import json

# Step 1: Read the JSON file
with open('C:\\work/JsonFile.json', 'r') as file:
    data = json.load(file)

# Step 2: Modify the data structure

data = data[0]
objects = data['objects']

for key in objects:
    print(key[''])

# Step 3: Write the updated data back to the JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
