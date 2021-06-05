from selenium import webdriver
import time
from basics import commons

"""
1.open browser
2.navigate to google website
3.take screenshot
4.close browser

 how to take screenshot ?
driver.save_screenshot("test.png")


"""
# get driver
driver = webdriver.Chrome(executable_path=commons.driver_url)

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)

print("******************get screenshot ******************************")
driver.save_screenshot("test.png")
time.sleep(5)
#close driver
driver.close()