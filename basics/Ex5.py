from selenium import webdriver
import time



"""
1.open browser
2.navigate to ggogle website 
3.close browser



step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()

 maximize_window ,Refresh , forward, back 

"""
from basics import commons
# get driver
driver = webdriver.Chrome(executable_path=commons.driver_url)

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)


#maximize window
driver.maximize_window()
time.sleep(5)


#refresh
driver.refresh()
#driver.minimize_window()

#Open gmail
driver.get("https://gmail.com")
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)


driver.forward()
print(driver.title)
time.sleep(5)


#close driver
driver.quit()