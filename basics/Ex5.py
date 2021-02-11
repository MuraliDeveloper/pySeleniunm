from selenium import webdriver
import time



"""
1.open browser
2.navigate to ggogle website 
3.close browser


How to maximize the window?
driver.maximize_window()

How to refresh the window?
driver.refresh()

How to perform back operation on a page?
driver.back()

How to perform forward operation on a page?
driver.forward()

step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()

 maximize_window ,Refresh , forward, back 

"""
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path ="C:\Murali\Training\Selenium\chromedriver_win32\chromedriver.exe" )

driver.get("https://www.google.co.in")
print(driver.title)
time.sleep(3)



driver.maximize_window()
print("after maximize_window",driver.title)
time.sleep(3)

#refresh
driver.refresh()
print(driver.title)
print("after refresh",driver.title)
time.sleep(3)

driver.get("https://www.gmail.co.in")
print(driver.title)
time.sleep(3)



driver.back()
print("after back",driver.title)
time.sleep(3)

driver.forward()
print(driver.title)
print("after forward",driver.title)
time.sleep(3)


#close driver
driver.close()