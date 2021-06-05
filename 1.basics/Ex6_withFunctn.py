"""

Req:
1.open browser
2.navigate to google website  (https://www.google.com)
3.close browser


"""
from selenium import webdriver
import time

from basics.commons import getChromeDriver

driver =  getChromeDriver()

driver.get("https://www.google.co.in")

time.sleep(5)

driver.close()
