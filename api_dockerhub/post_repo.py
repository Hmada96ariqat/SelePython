import json
import requests
# from utils import generate_random_string

# load the credintials from the config file
with open("config.json", "r") as file:
    config = json.load(file)

# Read the JWT token from the file
with open("jwt_token.txt", "r") as file:
    jwt_token = file.read().strip()

# REVISIT REASON 'try to random the repo_name'
# Set up the API request to create a new repository
repo_name = "xrrrddssf"
repo_description = "This is a new repository created via the API."
username = config["first_USERNAME"]


# DockerHub API URL to create a new repository
create_repo_url = f"https://hub.docker.com/v2/repositories/{username}/"

# Payload with the repository details
payload = {
    "name": repo_name,
    "description": repo_description,
    "is_private": False
}

# Headers including the Authorization token
headers = {
    "Authorization": f"JWT {jwt_token}",
    "Content-Type": "application/json"
}

# Step 3: Make the POST request to create the repository
response = requests.post(create_repo_url, headers=headers, json=payload)

# Step 4: Check the raw response content
if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully!")
else:
    print(f"Failed to create repository. Status code: {response.status_code}")
    print("Raw Response Text:", response.text)  # Print the raw response content
