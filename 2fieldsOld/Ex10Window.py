from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("")


currWinName = driver.current_window_handle # parent win name

allWindows =  driver.window_handles # all winnames

driver.switch_to.window(currWinName)

if driver.title =="facebook":
    driver.close() #close only specific window


driver.quit() #close all windows