from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from basics.commons import getChromeDriver

user = "abc"
pwd = "xyz"
driver = getChromeDriver()
driver.get("http://www.facebook.com")
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