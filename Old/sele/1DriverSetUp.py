#!/usr / bin / env python 
from selenium import webdriver 
import time 
  
# set webdriver path here it may vary 
brower = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
#brower = webdriver.Firefox(executable_path ="C:\Murali\chromedriver.exe")
#brower = webdriver.Ie(executable_path ="C:\Murali\chromedriver.exe")



website_URL ="https://www.google.co.in/"
brower.get(website_URL) 
print(brower.title)
print(brower.current_url)

time.sleep(4) 
brower.refresh()   
    
#get page source
html = brower.page_source
print(html)

brower.quit()