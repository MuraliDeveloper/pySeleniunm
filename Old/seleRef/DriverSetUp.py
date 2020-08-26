#!/usr / bin / env python 
from selenium import webdriver 
import time 
  
# set webdriver path here it may vary 
brower = webdriver.Chrome(executable_path ="C:\Murali\Training\chromedriver_win32\chromedriver.exe")

website_URL ="https://www.google.co.in/"
brower.get(website_URL) 
  
# After how many seconds you want to refresh the webpage 
# Few website count view if you stay there 
# for a particular time 
# you have to figure that out 
refreshrate = int(15) 
  
# This would keep running until you stop the compiler. 
while True: 
    time.sleep(refreshrate) 
    brower.refresh()
 