# Import the requests module
# It is used to send HTTP requests such as GET, POST, PUT, and DELETE.
import requests

# Note:
# If the requests library is not installed, install it using:
# pip install requests

# Send an HTTP GET request to the specified API endpoint.
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check whether the request was successful.
# A status code of 200 indicates that the server processed the request successfully.
if response.status_code == 200:

    # Convert the JSON response into a Python dictionary
    # using the json() method.
    data = response.json()

    # Display the title field from the response.
    print("GET Request successful. Title:", data['title'])
