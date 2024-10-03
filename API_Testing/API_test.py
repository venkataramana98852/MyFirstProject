import requests
import json
import jsonpath

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

response = requests.get(url)
json_response = json.loads(response.text)

# Use jsonpath to extract the list of 'id' values
ids = jsonpath.jsonpath(json_response, "$..id")

if ids:
    print(json_response[0]["title"])  # This will print the first 'id' from the list
else:
    print("No 'id' found")
url_post = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

# Data to send in the POST request
post_data = {
    "id": 0,
    "title": "Venkat Activity",
    "dueDate": "2024-09-01T00:00:00Z",
    "completed": False
}

# Perform the POST request
response_post = requests.post(url_post, json=post_data)

# Check the status code and print the response
if response_post.status_code == 200:
    print("POST request successful!")
    print("Response from POST request:")
    print(response_post.json())  # Print the JSON data returned by the server
else:
    print(f"Failed to post data. Status code: {response_post.status_code}")
    print(f"Response: {response_post.text}")

# URL for the DELETE request
url_delete = "https://fakerestapi.azurewebsites.net/api/v1/Activities/2"

# Perform the DELETE request
response_delete = requests.delete(url_delete)

# Check the status code and handle the response
if response_delete.status_code == 204:
    print("DELETE request successful!")
    print("No content to display from DELETE request.")
elif response_delete.status_code == 200:
    try:
        print("DELETE request successful with response content!")
        print("Response from DELETE request:")
        print(response_delete.json())  # Print the JSON data returned by the server (if any)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON.")
        print(f"Response content: {response_delete.text}")
else:
    print(f"Failed to delete data. Status code: {response_delete.status_code}")
    print(f"Response: {response_delete.text}")