from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://facebook.com")
t.sleep(300)
driver.quit()
