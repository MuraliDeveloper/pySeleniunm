from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


# get driver


def validateLabel(idriver, lables):
    for l,v in lables.items():
        element=idriver.find_element_by_id(l)
        assert v==element.text,"Lable value for {} is wrong".format(l)
    
driver= None
try:
    driver = webdriver.Chrome(executable_path="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
    
    driver.get("http://localhost:7080/fb/welcome.html")
    
    assert "Home Page"==driver.title , "Title value is wrong"
    
    labels = {"lname" : "Name :" ,
              "lpswd" : "Password :",
              "lgender" : "Gender :",
              "llocation" : "Cities :",
              "lcheck" : "Proofs"
              }
    validateLabel(driver,labels)
    
    
    nameField= driver.find_element_by_name("username")
    assert nameField.get_attribute("value")=="testUser", "Invalid default userName"
    passwordField = driver.find_element_by_name("password")
    
    nameField.clear()
    nameField.send_keys("Admin")
    passwordField.send_keys("Aadmin123")
    time.sleep(5)
    
    #check male is seleceted
    radio = driver.find_element_by_id("genderm")
    assert radio.is_selected() ,"Gender male should be selected"
    # radio female is selected
    radio = driver.find_element_by_id("genderf")
    radio.click()
    
    
    #test checkbox
    ch1  =driver.find_element_by_name("passport")
    assert ch1.is_displayed() ,"passport should be displayed"
    assert ch1.is_enabled() ,"passport should be enabled"
    ch1.click()
    ch1  =driver.find_element_by_name("voter")
    ch1.click()
    
    
    
    #test on dropdown
    cityDropdown = Select(driver.find_element_by_name("cities"))
    
    assert len(cityDropdown.options)==4 , "expected 4 cities"
    list =["Bangalore","Chennai","Mumbai","Hyderabad"]
    #select
    i=0
    for op in cityDropdown.options:
        #print(op.get_attribute("value"))
        assert op.text==list[i],"Invalid city :" + op.text
        i= i+1
    
    #SELECT
    cityDropdown.select_by_index(1)
    cityDropdown.select_by_visible_text("Mumbai")
    cityDropdown.select_by_value("HYD")
    
    print(cityDropdown.all_selected_options[0].text)
    
    #click on submit button
    button  =driver.find_element_by_name("submit")
    button.click()
    
    #click on link
    #link = driver.find_element_by_id("googleLink")
    #link = driver.find_element_by_link_text("Click for googlepage")
    link = driver.find_element_by_partial_link_text("googlepage")
    assert link.get_attribute("href")=="https://www.google.co.in/", "invalid URL" 
    link.click()
finally:
    time.sleep(5)
    driver.quit()

