from ast import Delete
from inspect import stack
from lib2to3.pgen2 import token
from msilib.schema import Class, PublishComponent
from multiprocessing.managers import Token
from platform import architecture
from pydoc import doc
import random as rd
from select import select
from tkinter.tix import MAIN
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import string
from cryptography.fernet import Fernet
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())

class  CreateDeleteRepo():
    
    def logIn(self):

        # Navigate to DockerHub.com with valid credintials
        # driver_1 = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://hub.docker.com/"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(15)
        driver.find_element("xpath", '//*[@id="signupForm"]/div[1]/div/div/div[2]/a').click()
        driver.find_element('xpath', '//*[@id="username"]').send_keys('hmada96')
        driver.find_element('xpath', '/html/body/div[2]/main/section/div/div/div/form/div[2]/button').click()
        driver.find_element('xpath', '//*[@id="password"]').send_keys('Dockerhub1')
        driver.find_element('xpath', '/html/body/div[2]/main/section/div/div/div/form/div[2]/button').click()
        driver.implicitly_wait(15)
        driver.find_element('xpath', '//*[@id="onetrust-reject-all-handler"]').click()

class CreateDeleteRepo_1():

    def repoCreation(self):
        # Create a new repo
        driver.implicitly_wait(15)
        driver.find_element('xpath', '//*[@id="mainContainer"]/div/div/div/div[1]/div[1]/span/button').click()

        # size of string(repo's name) 
        # generating random strings
        N = 7
        random_name = ''.join(rd.choices(string.ascii_lowercase + string.digits, k=N))
        driver.find_element('xpath', '/html/body/div/div[1]/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div[2]/div[1]/div[2]/div/input').send_keys(random_name)
        driver.find_element('xpath', '/html/body/div/div[1]/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div[2]/div[2]/div/input').send_keys('repo_desc')
        driver.find_element('xpath', '/html/body/div/div[1]/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/button[2]').click()
        driver.implicitly_wait(15)

        # Delete the same created repo
        driver.find_element('xpath', '//*[@id="mainContainer"]/div/div/div[2]/div/div/div/div/button[6]').click()
        element = driver.find_element('xpath', '/html/body/div[1]/div[1]/div/div[3]/div/div/div[3]/div/div[3]/div[2]/div/span/button')
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.perform()
        driver.find_element('xpath', '/html/body/div[1]/div[1]/div/div[3]/div/div/div[3]/div/div[3]/div[2]/div/span/button').click()
        driver.find_element('xpath', '//*[@id="imageNameField"]').send_keys(random_name)

        driver.save_screenshot("DeletedRepo.png")

        driver.implicitly_wait(15)
        driver.find_element('xpath', '/html/body/div[5]/div/div/div/div[3]/div[3]/button[2]').click()
        print(driver.current_url)
        driver.implicitly_wait(15)

        # Log-out
        driver.find_element('id', 'loggedInMenu').click()
        driver.implicitly_wait(15)
        driver.find_element('xpath', '/html/body/div/div[1]/div/div[2]/header/nav/div[2]/div/ul/li[5]').click()
        driver.implicitly_wait(15)
        print('success/wait to the next part')
        driver.close()

class explore():

    def exp(self):

      # Navigate to DockerHub.com with valid credintials
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://hub.docker.com/"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(15)
        driver.find_element("xpath", '//*[@id="signupForm"]/div[1]/div/div/div[2]/a').click()
        driver.find_element('xpath', '//*[@id="username"]').send_keys('hmada96')
        driver.find_element('xpath', '/html/body/div[2]/main/section/div/div/div/form/div[2]/button').click()
        driver.find_element('xpath', '//*[@id="password"]').send_keys('Dockerhub1')
        driver.find_element('xpath', '/html/body/div[2]/main/section/div/div/div/form/div[2]/button').click()
        driver.implicitly_wait(15)
        driver.find_element('xpath', '//*[@id="onetrust-reject-all-handler"]').click()
    
        # navigate to search bar and search for jenkins
        search_query = "jenkins/jenkins"
        xpath_value = '//*[@id="mui-1"]'
        driver.find_element('xpath', xpath_value).send_keys(search_query)
        driver.find_element('xpath', xpath_value).send_keys(Keys.RETURN)
        driver.implicitly_wait(25)
        print('Docker Pull Command copied!')
        driver.find_element('xpath', '//*[@id="searchResults"]/div/a[1]/div').click()
        driver.find_element('xpath', '//*[@id="mainContainer"]/div/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/code').click()
        driver.implicitly_wait(20)

        # navigate to explore page
        driver.find_element('xpath', '//*[@id="app"]/div[1]/div/div[2]/header/nav/a[1]').click()
        driver.find_element('xpath', '//*[@id="productTypeFilterList"]/div/label[1]/span[1]/input').click()
        driver.find_element('xpath', '//*[@id="operatingSystemsFilterList"]/div/label[1]/span[1]/input').click()
        element = driver.find_element('xpath', '//*[@id="architecturesFilterList"]/div/label[7]/span[1]/input')
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.perform()
        dropDown = driver.find_element('xpath', '//*[@id="mainContainer"]/div/div/div/div[2]/div[1]/div[2]/div/div')
        actions = ActionChains(driver)
        actions.move_to_element(dropDown)
        actions.perform()
        print('succeeded!')

# MAIN
CreateDeleteRepo().logIn()

CreateDeleteRepo_1().repoCreation()

explore().exp()

