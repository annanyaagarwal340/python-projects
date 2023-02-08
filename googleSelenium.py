from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time
#set chromodriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
#identify search box
m = driver.find_element(By.NAME,'q')
#enter search text
m.send_keys("Tutorialspoint")
time.sleep(2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
time.sleep(2)