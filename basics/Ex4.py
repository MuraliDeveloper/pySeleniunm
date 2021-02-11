from selenium import webdriver
import time
from basics import commons

"""
1.open browser
2.navigate to ggogle website
3. add cookie to webpage
3.close browser

Every cookie has name and value.
 
How to add cookie?
cookie = {"name" :"kumar", "value" : "1234"}
driver.add_cookie(cookie)

how to Fetch the cookies
cookies = driver.get_cookies()?


# Now set the cookie. This one's valid for the entire domain
cookie = {"name" :"kumar", "value" : "1234"}
driver.add_cookie(cookie)



How to get specific cookie?
c1 = driver.get_cookie("kumar")
print(c1['name'])
print(c1['value'])


How to delete specific cookie?
driver.delete_cookie("test")

How to delete all cookies?
driver.delete_all_cookies()

step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()


 

print("******************delete specific cookie ******************************")
driver.delete_cookie("test")

print("******************delete all cookies******************")


"""
# get driver
driver = webdriver.Chrome(executable_path=commons.driver_url)

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)

print("******************Get all cookies ******************************")
#get all cookies
cookies = driver.get_cookies()
for c in cookies:
     print(c['name'])
     print(c['value'])



time.sleep(5)

#close driver
driver.quit()
driver.close()