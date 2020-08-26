from selenium import webdriver
import time

# get driver

driver= None
try:
    driver = webdriver.Chrome(executable_path="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
    driver.get("http://localhost:7080/fb/test3.html")
    time.sleep(5)
    win1 = driver.window_handles[0]
   
    print(driver.title)
    driver.find_element_by_id("gLink1").click()
    print(driver.title)

    win1 = driver.window_handles[0]

    win2 = driver.window_handles[1]
    
    driver.switch_to.window(win2)
    print(driver.title)
    
    driver.switch_to.window(win1)
    print(driver.title)
    
    time.sleep(5)
finally:
    time.sleep(5)
    driver.quit()

