from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""
implicit wait -> [time based] chance of exceotion if the element is nit loaded withoin 10 sec
explicit wait  -> [upon the element is available not time based.]
wait for the element applicable for only 




"""
user = "abc"
pwd = "xyz"
driver = webdriver.Chrome('C:\\Murali\\Training\\chromedriver_win32\\chromedriver.exe')
driver.get("http://www.facebook.com")

driver.implicitly_wait(10)
"""
An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0. 
Once set, the implicit wait is set for the life of the WebDriver object.
"""
# wait for 10 seconds applicable for all the elements present in the page
#required for waiting for the page element

assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
print(elem.is_enabled())
print(elem.is_displayed())
print(elem.is_selected())#only for radio, select boxes



elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()