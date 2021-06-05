from selenium import webdriver
import time
"""
 
1.open browser
2.navigate to google website 
3.close browser

Step1: 
get driver object using the driver software
 
Q)How to create the driver object?
Ans)
from selenium import webdriver
driver = webdriver.Chrome(executable_path ="<driver path>" )



Step2: 
access any url using driver obj .
use get() method


Q)How to open any web page?
ans)
driver.get("https://www.google.co.in")



Step3: 
driver.close()

Q)How to close the driver?
Ans)
driver.close()

"""


# get driver
driver = webdriver.Chrome(executable_path="C:\Murali\Training\Selenium\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path ="C:\Murali\firefox.exe")
#driver = webdriver.Ie(executable_path ="C:\Murali\ie.exe")

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)

driver.close()