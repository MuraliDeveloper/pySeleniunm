from selenium import webdriver
import time

# get driver
driver = webdriver.Chrome(executable_path="C://Users//NareshT//Downloads//chromedriver.exe")

# open google.com
driver.get("https://www.google.co.in")
time.sleep(5)
driver.get("https://www.gmail.co.in")
print()
time.sleep(5)
driver.close()
