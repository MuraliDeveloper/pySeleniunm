from selenium import webdriver
import time
from basics import commons
"""
Req:
1.open browser
2.navigate to google website  (https://www.google.com)
3.print page url , title ,  session_id  , driver name ,
4.close browser


How to access the page title?
print(driver.title)
 

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
