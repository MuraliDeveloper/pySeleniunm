#!/usr / bin / env python
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# set webdriver path here it may vary
browser = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")



browser.get("https://google.com")
print(browser.title)
input = browser.find_element_by_id("searchInput")
input.send_keys("Python")
input.send_keys(Keys.ENTER)


browser.close()
