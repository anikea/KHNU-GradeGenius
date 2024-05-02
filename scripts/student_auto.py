import os
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv(find_dotenv())


# змінити на свої вхідні дані
password = os.getenv('pass')
login = os.getenv('login')


driver = webdriver.Firefox()

driver.get('https://khmnu.edu.ua/')

time.sleep(0.5)

eu = driver.find_element(By.ID, "menu-item-21")
eu.click()

vxid = driver.find_element(By.CLASS_NAME, 'link-item3')
vxid.click()

login_input = driver.find_element(By.ID, "login")
login_input.send_keys(login)

time.sleep(0.5)

password_input = driver.find_element(By.ID, "passwd")
password_input.send_keys(password)

time.sleep(0.5)

lesgo = driver.find_element(By.CLASS_NAME, "S4")
lesgo.click()

time.sleep(0.5)


actions = ActionChains(driver)


dropdown1 = driver.find_element(By.CSS_SELECTOR, '#mi_0_5 > div:nth-child(1)')


actions.move_to_element(dropdown1).perform()


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#mi_0_6 > div:nth-child(1)")))


item_to_clk = driver.find_element(By.CSS_SELECTOR, "#mi_0_6 > div:nth-child(1)")
item_to_clk.click()

time.sleep(0.5)

journal = driver.find_element(By.CSS_SELECTOR, "#MainTab > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > a:nth-child(1)")
journal.click()

final = driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(2) > p:nth-child(28) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(5) > a:nth-child(1)")
final.click()
