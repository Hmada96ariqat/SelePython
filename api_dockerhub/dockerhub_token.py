import json
import requests


# load the credintials from the config file
with open("config.json", "r") as file:
    config = json.load(file)

# Replace these with your actual DockerHub username and password
username = config["first_USERNAME"]
password = config["first_PASSWORD"]

# The login URL for DockerHub's API
URL = "https://hub.docker.com/v2/users/login/"

# Payload containing your credentials
payload = {
    "username": username,
    "password": password
}

# Make the POST request to login and get the JWT token
response = requests.post(URL, json=payload)

# Check if login was successful
if response.status_code == 200:
    # Extract the token from the response
    jwt_token = response.json().get("token")

    # Write the JWT token to a file
    with open("jwt_token.txt", "w") as file:
        file.write(jwt_token)

    print("JWT Token has been written to jwt_token.txt")
else:
    print(f"Failed to login. Status code: {response.status_code}")
    print("Response:", response.json())
