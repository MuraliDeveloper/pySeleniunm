from selenium import webdriver
import time

#ByName
driver = webdriver.Firefox()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(5)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Techbeamers")
inputElement.submit()
time.sleep(20)

driver.close()

#ById
driver.get("http://google.com")
driver.maximize_window()
time.sleep(5)
inputElement = driver.find_element_by_id("lst-ib")
inputElement.send_keys("Techbeamers")
inputElement.submit()
time.sleep(20)

driver.close()

#By Link Text
driver = webdriver.Firefox()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(5)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Techbeamers")
inputElement.submit()
time.sleep(5)
elem = driver.find_element_by_link_text("Python Tutorial")
elem.click()
time.sleep(20)

driver.close()

# By Partial Link Text
driver = webdriver.Firefox()
driver.get("http://google.com")
driver.maximize_window()
time.sleep(5)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("Techbeamers")
inputElement.submit()
time.sleep(5)
elem = driver.find_element_by_partial_link_text("Python")
elem.click()
time.sleep(20)

driver.close()

#By Xpath
"""
<html>
<body>
<form id="signUpForm">
<input name="emailId/mobileNo" type="text" />
<input name="password" type="password" />
<input name="continue" type="submit" value="SignUp" />
<input name="continue" type="button" value="Clear" />
</form>
</body>
<html>
"""
form_element = driver.find_element_by_xpath("/html/body/form[1]")
form_element = driver.find_element_by_xpath("//form[1]")
form_element = driver.find_element_by_xpath("//form[@id='signUpForm']")
email_input = driver.find_element_by_xpath("//form[input/@name='emailId/mobileNo']")
email_input = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
email_input= driver.find_element_by_xpath("//input[@name='emailId/mobileNo']")

#By CSS Selector
"""
<html>
<body>
<div class="round-button">Click Here</p>
</body>
<html>
"""

get_div = driver.find_element_by_css_selector('div.round-button')


#By Tagname
"""
<html>
<body>
<title>Hello Python</title>
<p>Learn test automation using Python</p>
</body>
"""
get_div = driver.find_element_by_tag_name('title')

#By Classname
"""
<html>
<body>
<div class="round-button">Click Here</div>
</body>
<html>
"""
get_div = driver.find_element_by_class_name('round-button')


#By id, name ,xpath
#<input type="text" name="user" id="user_name" />
element = driver.find_element_by_id("user_name")
element = driver.find_element_by_name("user")
element = driver.find_element_by_xpath("//input[@id='user_name']")
