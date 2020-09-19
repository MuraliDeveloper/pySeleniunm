from   selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.facebook.com")
  
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
submit   = browser.find_element_by_id("submit")
  
username.send_keys("me")
password.send_keys("mykewlpass")
  
submit.click()
