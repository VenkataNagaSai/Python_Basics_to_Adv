# Import the json module
# It provides functions to convert Python objects to JSON and vice versa
import json

# Create a Python dictionary containing configuration data
data = {
    "model": "llama-3",
    "temperature": 0.7
}

# Convert the Python dictionary into a formatted JSON string
# indent=2 makes the JSON output more readable with 2-space indentation
json_str = json.dumps(data, indent=2)

# Display the JSON string
print("Dictionary to JSON String:\n", json_str)
