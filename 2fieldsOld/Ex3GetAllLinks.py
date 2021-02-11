#!/usr / bin / env python 
from selenium import webdriver

# set webdriver path here it may vary
from selenium.webdriver.common.by import By

brower = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
brower.get('https://www.w3.org/')
for a in brower.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))
brower.quit()


#find all links
links = brower.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    print(link.text)