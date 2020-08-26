import commons
from selenium import webdriver
import time

# get driver
driver = webdriver.Chrome(executable_path=commons.driver_url)
print(driver.name)




#open google.com

driver.get("https://www.google.co.in")

#maximum window
driver.maximize_window()
time.sleep(5)
print(driver.title)





driver.refresh()
time.sleep(5)
driver.get("https://youtube.com")
print(driver.title)



driver.back()
print(driver.title)
time.sleep(5)


driver.forward()
print(driver.title)
time.sleep(5)


driver.close()




