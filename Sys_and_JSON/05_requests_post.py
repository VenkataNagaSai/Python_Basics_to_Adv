# Import the requests module
# It is used to send HTTP requests (GET, POST, PUT, DELETE, etc.)
import requests

# Define the API endpoint where the POST request will be sent.
url = "https://jsonplaceholder.typicode.com/posts"

# Create the data (payload) to be sent to the server.
# Passing it through the 'json' parameter automatically converts
# the Python dictionary into JSON format.
payload = {
    "title": "VLSI Agent",
    "body": "Parsing test."
}

# Send an HTTP POST request with the JSON payload.
response = requests.post(url, json=payload)

# Check if the resource was created successfully.
# HTTP status code 201 indicates successful creation.
if response.status_code == 201:

    # Convert the JSON response into a Python dictionary
    # and display the server's response.
    print("POST Request successful. Server replied with:", response.json())
