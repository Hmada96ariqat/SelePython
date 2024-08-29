import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException  # Import TimeoutException



class DockerHubAutomation:
    
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "https://hub.docker.com/"
        self.username = 'hmada96'
        self.password = 'Dockerhub1'
        self.wait = WebDriverWait(self.driver, 30)  # Increased wait time to 30 seconds

    def navigate_to_login(self):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(15)
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()
        # Assertion to verify we are on the login page by checking for the presence of the username field
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        assert username_field.is_displayed(), "Username field is not displayed; not on the Sign In page."


    def log_in(self):
        self.navigate_to_login()
        self.wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(self.username)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        self.wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        self.wait.until(EC.presence_of_element_located((By.ID, 'onetrust-reject-all-handler'))).click()
        # Assertion to verify that login was successful by checking for a known element
        # time.sleep(5)
        # create_repo = self.wait.until(EC.presence_of_element_located((By.ID, 'createRepoBtn')))
        # assert create_repo.is_displayed(), "Login failed or repositories page not loaded."

    def create_repo(self):
        self.log_in()
        time.sleep(5)  # Sleep before clicking "Create Repository" button
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/span/button"))
        ).click()
        repo_name = self.generate_random_string(7)
        time.sleep(5)  # Sleep before entering repo details
        self.driver.find_element(By.XPATH, 
            '/html/body/div[2]/div/div[2]/div/div/div[1]/form/div/div[1]/div[2]/div/div/input'
        ).send_keys(repo_name)
        self.driver.find_element(By.XPATH, 
            '/html/body/div[2]/div/div[2]/div/div/div[1]/form/div/div[1]/div[3]/div/div/div/textarea[1]'
        ).send_keys('repo_desc')
        self.driver.find_element(By.XPATH, 
            '/html/body/div[2]/div/div[2]/div/div/div[1]/form/div/div[2]/span/button'
        ).click()
        # Assertion to verify the repository creation was successful
        # repo_created = self.wait.until(EC.presence_of_element_located(By., "Created less than a minute ago"))
        # user_and_repo = self.username + '/' + repo_name
        # assert user_and_repo.is_displayed(), "Repository creation failed."
        # return repo_name
        try:
            repo_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, f'//span[text()="{repo_name}"]'))
            )
            assert repo_element.is_displayed(), "Repository creation failed."
            print("IT WORKED!!!!!!")
        except TimeoutException:
            print("Repository not found or not displayed.")
   
        return repo_name

    def delete_repo(self, repo_name):
        time.sleep(5)  # Sleep before attempting to delete the repo
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/a[6]')
        )).click()
        element = self.driver.find_element(By.XPATH, 
            '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div[2]/span/button'
        )
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        self.wait.until(EC.presence_of_element_located((By.ID, 'imageNameField'))).send_keys(repo_name)
        self.driver.save_screenshot("DeletedRepo.png")
        self.driver.find_element(By.XPATH, 
            '/html/body/div[13]/div[3]/div/div[3]/button[2]'
        ).click()
        # Assertion to verify the repository deletion was successful
        # assert "Repository Deleted" in self.driver.page_source, "Repository deletion failed."

    def generate_random_string(self, length):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def run(self):
        repo_name = self.create_repo()
        self.delete_repo(repo_name)
        self.driver.quit()


# Example usage:
if __name__ == "__main__":
    automation = DockerHubAutomation()
    automation.run()
