from selenium import webdriver
import time
"""
Steps:
--------
1.Download the driver for the browser.
Python -----> Driver -----> Browser.

https://sites.google.com/a/chromium.org/chromedriver/

Extract the zip file

2. import the "selenium" package.
command:
pip install selenium

or install using pycharm

Steps:
----------------
1.create the driver object
2.open the web page
3.perform the navigation/actions/testing
4.close the driver


Q)How to create the driver object?
Ans)
from selenium import webdriver
driver = webdriver.Chrome(executable_path ="<driver path>" )


Q)How to open any web page?
ans)
driver.get("https://www.google.co.in")


Q)How to close the driver?
Ans)
driver.close()

"""

"""
1.open browser
2.navigate to google website 
3.close browser

step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()


"""
# get driver
driver = webdriver.Chrome(executable_path="C:\Murali\Training\Selenium\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path ="C:\Murali\firefox.exe")
#driver = webdriver.Ie(executable_path ="C:\Murali\ie.exe")

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)

driver.close()