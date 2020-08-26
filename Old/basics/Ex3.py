from selenium import webdriver
import time

# get driver


driver= None
try:
    driver = webdriver.Chrome(executable_path="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
    
    driver.get("http://localhost:7080/fb/test.html")
    
    f1= driver.find_element_by_xpath("//*[@id='signUpForm']/input[1]")
    f1.send_keys("Hello")
    
    f2=driver.find_element_by_css_selector("div.round-button")
    assert "Users Info"==f2.text ,"Invalid label"
    
    f2=driver.find_element_by_tag_name("myTag")
    print("tag value: ",f2.text)
finally:
    time.sleep(5)
    driver.quit()

