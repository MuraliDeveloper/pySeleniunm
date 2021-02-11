#!/usr / bin / env python 
from selenium import webdriver

# set webdriver path here it may vary 
brower = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe") 
#or
#brower = webdriver.Chrome(chrome_driver_path)
  
# create a new Chrome session
brower.implicitly_wait(30)
brower.maximize_window()
#find element by id
brower.get('http://codepad.org')
text_area = brower.find_element_by_id('textarea')
text_area.send_keys("This text is send using Python code.") 
text_area.clear()
text_area.send_keys("test1")

brower.quit()