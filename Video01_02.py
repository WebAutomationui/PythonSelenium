from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="E://Automation//chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
searchBox = driver.find_element_by_css_selector("input[name='q']")
searchBox.clear()
searchBox.send_keys("selenium")
searchBox.send_keys(Keys.RETURN)
time.sleep(10)
driver.close()
driver.quit()