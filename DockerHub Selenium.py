from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# Navigate to DockerHub.com with valid credintials
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://hub.docker.com/")
driver.find_element_by_xpath('//*[@id="signupForm"]/div[1]/div/div/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('hmada96')
driver.find_element_by_xpath('/html/body/div[2]/main/section/div/div/div/form/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Weezyfbaby1')
driver.find_element_by_xpath('/html/body/div[2]/main/section/div/div/div/form/div[2]/button').click()
driver.implicitly_wait(5)

# Create a new repo
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/button/span').click()
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div[2]/div[1]/div[2]/div/input').send_keys('python_repo_1')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div[2]/div[2]/div/input').send_keys('repo_desc')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/button[2]').click()
driver.implicitly_wait(5)

# Delete the same created repo
driver.find_element_by_xpath('//*[@id="module-repository-detail"]/div[2]/div/div/button[6]').click()
element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div/div[3]/div/div[3]/div/div/button')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div/div/div[3]/div/div[3]/div/div/button').click()
driver.find_element_by_xpath('//*[@id="imageNameField"]').send_keys('python_repo_1')
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/div[3]/button[2]').click()
print(driver.current_url)
driver.implicitly_wait(5)

# Log-out
driver.find_element_by_id('loggedInMenu').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/header/nav/div[2]/div/ul/li[5]').click()
driver.implicitly_wait(5)
driver.close()