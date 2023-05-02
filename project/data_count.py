import json

# Load the JSON file
with open("/depot/davisjam/data/wenxin/CS577-NLP/project/squad_format_data.json", "r") as f:
    data = json.load(f)

# Count the number of data
num_data = len(data["data"])

# Print the result
print("Number of data:", num_data)
