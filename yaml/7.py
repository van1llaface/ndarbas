import json

# File path
file_path = "7.json"

# Step 1: Read JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)  # Load JSON into a Python dictionary

# Step 2: Modify the data
# Change the value of "name" if it exists
data["name"] = "Stasys"

# Add a new field "new_field"
data["Favorite color"] = "Green"

# Delete the "age" field if it exists
if "age" in data:
    del data["age"]

# Step 3: Write the updated data back to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)  # Save the data back to the file with pretty formatting

print(f"JSON data updated successfully in {file_path}.")
