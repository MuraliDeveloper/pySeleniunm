from selenium import webdriver
import time
from basics import commons

"""
1.open browser
2.navigate to ggogle website 
3.close browser


step1: get driver object using the driver software
step2: access any url using driver obj .
get() method
step3: driver.close()


Fetch the cookies

"""
# get driver
driver = webdriver.Chrome(executable_path=commons.driver_url)

#open google.com
driver.get("https://www.google.co.in")
time.sleep(5)

# Now set the cookie. This one's valid for the entire domain
cookie = {"name" :"foo", "value" : "bar"}
driver.add_cookie(cookie)

print("******************Get all cookies ******************************")
#get all cookies
cookies = driver.get_cookies()
for c in cookies:
     print(c['name'])
     print(c['value'])


print("******************Get specific cookie ******************************")
#get specific cookie
c1 = driver.get_cookie("NID")
print(c1['name'])
print(c1['value'])



print("******************delete specific cookie ******************************")
driver.delete_cookie("test")


print("******************delete all cookies******************")
driver.delete_all_cookies()


time.sleep(5)

#close driver
driver.quit()
driver.close()