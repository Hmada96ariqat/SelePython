"""
create_delete_repo.py

This module provides functions to create and delete the repository using Selenium WebDriver.

Functions:
- create_repo(driver, wait, generate_random_string, log_in):
  Creates a new repository with a randomly generated name.

- delete_repo(driver, wait, repo_name):
  Deletes the specified repository.

Parameters:
- wait (WebDriverWait): WebDriverWait instance for element waits.
- generate_random_string (function): Function to generate a random repository name.
- log_in (function): Function to log into DockerHub.
- repo_name (str): Name of the repository to delete.

Exceptions:
- TimeoutException: Raised on timeout during operations.
- Exception: Raised for other errors.

Author: Adam Areiqat
Date: August 2024
"""


import logging
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# load the credintials from the config file
with open("config.json", "r") as file:
    config = json.load(file)

def create_repo(driver, wait, generate_random_string, log_in):
    try:
        logging.info("Attempting to create a repository.")
        # Credintials for logging in
        username = config["first_USERNAME"]
        password = config["first_PASSWORD"]
        log_in(driver, wait, username, password)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='createRepoBtn']"))
        ).click()
        repo_name = generate_random_string(7)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='repoNameField-input']"
        ).send_keys(repo_name)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='repoDescriptionField-input']"
        ).send_keys('repo_desc')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='submit']"
        ).click()
        return repo_name
    except TimeoutException as e:
        logging.error("Repository creation failed due to timeout: %s", e)
        raise
    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise

def delete_repo(driver, wait, repo_name):
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[data-testid='tabSettings']")
    )).click()
    element = driver.find_element(By.CSS_SELECTOR, "[data-testid='deleteRepo']")
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    wait.until(EC.presence_of_element_located((By.ID, 'imageNameField'))).send_keys(repo_name)
    driver.save_screenshot("DeletedRepo.png")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='confirm']").click()
