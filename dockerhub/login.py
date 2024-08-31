# login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_login(driver, wait, base_url):
    driver.get(base_url)
    driver.implicitly_wait(15)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    assert username_field.is_displayed(), "Username field is not displayed."

def log_in(driver, wait, username, password):
    URL = "https://hub.docker.com/"
    navigate_to_login(driver, wait, URL)
    wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(username)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    wait.until(EC.presence_of_element_located((By.ID, 'onetrust-reject-all-handler'))).click()
