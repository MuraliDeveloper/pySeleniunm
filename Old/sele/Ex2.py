#!/usr / bin / env python 
from selenium import webdriver 
import time 
  
# set webdriver path here it may vary 
brower = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe") 
#or
#brower = webdriver.Chrome(chrome_driver_path)
  
# create a new Chrome session
brower.implicitly_wait(30)
brower.maximize_window()
website_URL ="https://www.google.co.in/"
brower.get(website_URL) 
  
time.sleep(5) 
brower.refresh()

brower.quit()