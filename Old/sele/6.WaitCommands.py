from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
implicit wait -> [time based] chance of exceotion if the element is nit loaded withoin 10 sec
explicit wait  -> [upon the element is available not time based.]
wait for the element applicable for only 



"""
user = "abc"
pwd = "xyz"
driver = webdriver.Chrome('C:\\Murali\\Training\\chromedriver_win32\\chromedriver.exe')
driver.get("http://www.facebook.com")

driver.implicitly_wait(10)
# wait for 10 seconds applicable for all the elements present in the page
#required for waiting for the page element

assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
print(elem.is_enabled())
print(elem.is_displayed())
print(elem.is_selected())#only for radio, select boxes



elem.send_keys(user)

#create wait obj on driver and wait until the lement is located
#<input type="text" name="name" />
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
#This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds.
element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "name"))
    )

elem = driver.find_element_by_id("pass")
#elem = driver.find_element(By.ID,"pass")

elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()
"""
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

"""