from selenium import webdriver
import time
from basics import commons
"""
1.open browser
2.navigate to ggogle website 
3.close browser



step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()


print page url , title ,  session_id  , driver name , 

"""
# get driver
driver = webdriver.Chrome(executable_path=commons.driver_url)

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)


print(driver.current_url)
print(driver.title)
print(driver.session_id)
#print(driver.page_source)
print(driver.name)


time.sleep(5)
#close driver
driver.quit()
