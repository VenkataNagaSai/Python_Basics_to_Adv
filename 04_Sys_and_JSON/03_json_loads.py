# Import the built-in json module
# It provides functions to convert between JSON strings and Python objects.
import json

# Define a JSON-formatted string.
json_str = '{"status": "success", "tokens": 150}'

# Convert the JSON string into a Python dictionary.
# json.loads() deserializes a JSON string into a Python object.
data = json.loads(json_str)

# Display a heading for the output.
print("JSON String to Dictionary:")

# Access and print the value associated with the 'status' key.
print("Status:", data['status'])
