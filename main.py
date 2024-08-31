"""
main.py

This script serves as the entry point for automating
tasks on DockerHub using Selenium WebDriver.
It handles the setup and teardown of the WebDriver,
logs into DockerHub, creates a new repository,
and then deletes it.
The script utilizes modular functions
for better code organization and reusability.

Modules:
-setup_driver, teardown_driver (from dockerhub.fixture):
Handles WebDriver setup and cleanup.
-create_repo, delete_repo: Functions to create and delete a repository.
-generate_random_string (from utils.utils):
Generates a random string used as the repository name.
-log_in (from dockerhub.login):
Handles the login process.

Usage:
- Execute this script directly to run the full automation process.

Author: Adam Areiqat
Date: August 2024
"""


from dockerhub.fixture import setup_driver, teardown_driver
from dockerhub.create_delete_repo import create_repo, delete_repo
from dockerhub.login import log_in
from utils.utils import generate_random_string

def main():

    driver, wait = setup_driver()
    try:
        repo_name = create_repo(driver, wait, generate_random_string, log_in)
        delete_repo(driver, wait, repo_name)
    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    main()
