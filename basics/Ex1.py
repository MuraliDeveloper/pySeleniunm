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


"""
# get driver
driver = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path ="C:\Murali\firefox.exe")
#driver = webdriver.Ie(executable_path ="C:\Murali\ie.exe")

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)

driver.close()