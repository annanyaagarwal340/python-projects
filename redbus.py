from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
# create a new instance of the Firefox driver 
driver = webdriver.Chrome()
# navigate to the website 
driver.get("https://www.redbus.in/")
driver.implicitly_wait(300)
# locate the departure city form and fill in the desired city
departure_city_form = driver.find_element("id","src") 
departure_city_form.send_keys("Mumbai")
# locate the arrival city form and fill in the desired city 
arrival_city_form = driver.find_element("id","dest")
arrival_city_form.send_keys("Delhi") 
# locate the date of travel form and fill in the desired date 
date_form = driver.find_element(By.XPATH, '//*[@id="onward_cal"]')
date_form.click()
xpath='//td[contains(@class,"wd day")]'
date_form.find_element(By.XPATH,xpath).click()
#click on search button
button = driver.find_element("id","search_btn").click()
from datetime import datetime,timedelta
import time
time.sleep(2) 
presentday=datetime.now()
tommorow=presentday+timedelta(1)
t=str(tommorow)
driver.get("https://www.redbus.in/bus-tickets/mumbai-to-delhi?fromCityName=Mumbai&fromCityId=462&toCityName=Delhi&toCityId=733&onward="+t+"-Jan-2023&srcCountry=IND&destCountry=IND&opId=0&busType=Any")

sort_by_rating=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/a[1]').click()
time.sleep(3)
sort_by_fare=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[6]/a[1]').click()
time.sleep(3)
view_seats=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/div[1]/li[1]/div[1]/div[2]/div[1]').click()
time.sleep(5)
#phone_number=driver.find_element(By.CLASS_NAME,"IP").send_keys('187287219')
#time.sleep(3)
boarding=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/div[1]/li[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]').click()
time.sleep(3)
droping=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/div[1]/li[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/ul[1]/li[1]/div[1]/div[1]').click()
time.sleep(2)
#continuee=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/div[1]/li[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]').click()
#time.sleep(2)
proceed_to_book=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/ul[1]/div[1]/li[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[6]/button[1]').click()
time.sleep(2)
name=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/input[1]').send_keys('annanya agarwal')
age=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/label[1]/input[1]').send_keys('19')
gender=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span[2]/div[1]/div[1]').click()
email=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/label[1]/input[1]').send_keys('annanyaagarwal@gmail.com')
number=driver.find_element(By.XPATH,'//body[1]/section[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/label[1]/input[1]').send_keys('9839373872')
time.sleep(3)

