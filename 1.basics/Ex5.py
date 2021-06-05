from selenium import webdriver
import time



"""

1.open browser
2.navigate to google website 
4.perform page operations:
 - maximize
 - refresh
 - back
 - forward
 
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
"""
1.open browser
2.navigate to google website
3.perform page operations:
 - maximize
 - refresh
 - back
 - forward

4.close browser

"""

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path ="C:\chromedriver.exe")

driver.get("https://www.google.co.in")
print(driver.title)
time.sleep(3)

#maximize
driver.maximize_window()
time.sleep(3)

#refresh
driver.refresh()
print(driver.title)
time.sleep(3)

#open gmail
driver.get("https://www.gmail.co.in")
print(driver.title)
time.sleep(3)

#click on back
driver.back()
print("after back",driver.title)
time.sleep(3)


#click on forward
driver.forward()
print(driver.title)
print("after forward",driver.title)
time.sleep(3)

driver.close()
