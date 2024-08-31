# create_delete_repo.py

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def create_repo(driver, wait, generate_random_string, log_in):
    try:
        logging.info("Attempting to create a repository.")
        # Credintials for logging in
        username = 'hmada96'
        password = 'Dockerhub1'
        log_in(driver, wait, username, password)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/span/button"))
        ).click()
        repo_name = generate_random_string(7)
        driver.find_element(By.XPATH,
            '/html/body/div[2]/div/div[2]/div/div/div[1]/form/div/div[1]/div[2]/div/div/input'
        ).send_keys(repo_name)
        driver.find_element(By.XPATH,
            '/html/body/div[2]/div/div[2]/div/div/div[1]/form/div/div[1]/div[3]/div/div/div/textarea[1]'
        ).send_keys('repo_desc')
        driver.find_element(By.XPATH,
            '/html/body/div[2]/div/div[2]/div/div/div[1]/form/div/div[2]/span/button'
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
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/a[6]')
    )).click()
    element = driver.find_element(By.XPATH,
        '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/span/button'
    )
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    wait.until(EC.presence_of_element_located((By.ID, 'imageNameField'))).send_keys(repo_name)
    driver.save_screenshot("DeletedRepo.png")
    driver.find_element(By.XPATH, 
        '/html/body/div[13]/div[3]/div/div[3]/button[2]'
    ).click()
