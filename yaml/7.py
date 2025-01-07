import json

# Step 1: Read JSON data from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Parse the JSON data
    return data

# Step 2: Manipulate the JSON data
def manipulate_data(data):
    # Example manipulations:
    # 1. Change a value
    if "name" in data:
        data["name"] = "Updated Name"
    
    # 2. Add a new field
    data["Favorite color"] = "Green"
    
    # 3. Delete a field
    if "age" in data:
        del data["age"]
    
    return data

# Step 3: Write JSON data back to the file
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)  # Write JSON with pretty formatting

# Main Program
if __name__ == "__main__":
    file_path = "7.json"  # Path to your JSON file
    
    # Read the JSON file
    json_data = read_json_file(file_path)
    
    # Manipulate the data
    modified_data = manipulate_data(json_data)
    
    # Write the modified data back to the file
    write_json_file(file_path, modified_data)
    
    print(f"JSON data updated successfully in {file_path}.")
