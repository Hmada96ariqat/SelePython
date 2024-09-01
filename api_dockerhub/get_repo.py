import json
import requests

# Load the credentials from the config file
with open("config.json", "r") as file:
    config = json.load(file)

with open("jwt_token.txt", "r") as file:
    jwt_token = file.read().strip()

def test_get_repositories():
    username = config["first_USERNAME"]  # Replace with the DockerHub username you want to test
    url = f"https://hub.docker.com/v2/repositories/{username}/"

    # Headers including the Authorization token
    headers = {
        "Authorization": f"JWT {jwt_token}",
        "Content-Type": "application/json"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)  # Add headers here

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    response_data = response.json()  # Correct way to parse JSON

    # Check if 'results' key is in the response data
    assert 'results' in response_data, "Response does not contain 'results' key"
    assert len(response_data['results']) > 0, "No repositories found for the user"

    # Print out the names of the repositories for debugging purposes
    for repo in response_data['results']:
        print(f"Repository: {repo['name']}")

# Call the function to run the test
test_get_repositories()
