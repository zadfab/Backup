from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)/chromedriver")

driver.get("https://www.air.irctc.co.in/air-services/flight-ticket-reservation.html")

print(driver.title)

driver.get("https://www.facebook.com/")

print(driver.title)

driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.quit()