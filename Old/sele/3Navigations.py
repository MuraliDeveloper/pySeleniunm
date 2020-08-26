from selenium import webdriver
import time
"""
1.open browser
2.navigate to ggogle website 
3.close browser



step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()


"""
# get driver
driver = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)
print(driver.current_url)
# driver.delete_all_cookies()
# driver.delete_cookie("test")
# driver.get_cookie("test")
# cookies = driver.get_cookies()
# for c in cookies:
#     print(c['name'])
#     print(c['value'])
    
print(driver.title)
print(driver.session_id)
#print(driver.page_source)
print(driver.name)


time.sleep(5)


driver.refresh()
#driver.minimize_window()
driver.maximize_window()
driver.get("https://gmail.com")
print(driver.title)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)



time.sleep(5)
#close driver
driver.quit()
driver.close()