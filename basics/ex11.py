from selenium import webdriver

from basics import commons

"""
1.open browser
2.navigate to ggogle website 
3.close browser



step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()


"""
# get driver
driver = webdriver.Chrome(executable_path="C://Users//NareshT//Downloads//chromedriver.exe")

# open google.com
driver.get(commons.app_url + "drag.html")

driver.close()
