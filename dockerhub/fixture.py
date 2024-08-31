"""
fixture.py

Provides functions to set up and tear down the Selenium WebDriver for browser automation.

Functions:
- setup_driver():
  Initializes and returns a WebDriver instance and a WebDriverWait instance.

- teardown_driver(driver):
  Closes the WebDriver instance.

Returns:
- driver (webdriver.Chrome): WebDriver instance.
- wait (WebDriverWait): WebDriverWait instance.

Author: Adam Areiqat
Date: August 2024
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    return driver, wait

def teardown_driver(driver):
    driver.quit()
