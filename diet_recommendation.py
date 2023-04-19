import json


# Load the JSON data
with open('diet_dataset.json', 'r') as f:
    data = json.load(f)
    

# Define the threshold for the GI value

gi_threshold = 35

# Filter the diet data based on GI value
# filtered_diet_data = [item for item in data if item['GI'] <= gi_threshold]

# Print the filtered value
# print(json.dumps(filtered_diet_data, indent= 4))
print(data)