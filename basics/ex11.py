from selenium import webdriver

from basics import commons

"""
1.open browser
2.navigate to google website 
3.close browser



step1: get driver object using the driver software
step2: access any url using driver obj .
use get() method
step3: driver.close()


"""
# get driver
driver = webdriver.Chrome(executable_path="C://Murali//Training//Selenium//chromedriver_win32")

# open google.com
driver.get(commons.app_url + "drag.html")

driver.close()
