"""
login.py

This module provides functions for logging into DockerHub using Selenium WebDriver.
It includes:

- navigate_to_login(driver, wait, base_url): Navigates to the login page
- log_in(driver, wait, username, password):
    Logs in to DockerHub by entering the username and password,
    then handling post-login actions.

Usage:
- Call `log_in()` with the WebDriver instance, wait object, username, and password
    to perform the login process.

Author: Adam Areiqat
Date: August 2024
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def navigate_to_login(driver, wait, base_url):
    driver.get(base_url)
    driver.implicitly_wait(15)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    assert username_field.is_displayed(), "Username field is not displayed."

def log_in(driver, wait, username, password):
    url = "https://hub.docker.com/"
    navigate_to_login(driver, wait, url)
    username_element = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    username_element.send_keys(username)
    username_element.send_keys(Keys.ENTER)
    password_element = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_element.send_keys(password)
    password_element.send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.ID, 'onetrust-reject-all-handler'))).click()
