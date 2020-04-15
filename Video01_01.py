from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="E://Automation//chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.close()
driver.quit()