from selenium import webdriver
import time

"""
 <!DOCTYPE html>
<html>
<body bgcolor="#E6E6FA">
<h1>
Employee Login</h1>
<button onclick="myFunction()"name ="employeeLogin">Continue</button>

<p id="msg">
</p>
<script>
function myFunction() {
 var login = prompt("Please re-enter your name", "xxxxxx");
 
 if (login != null) {
 document.getElementById("msg").innerHTML =
 "Welcome " + login + "!! How can I help you?";
 alert("You have logged in successfully !!")
 }
}
</script>
</body>
</html>
"""

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
location = "file://<Specify Path to Prompt_Alert.HTML>"
driver.get(location)

#Click on the "employeeLogin" button to generate the Prompt Alert
button = driver.find_element_by_name('continue')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

time.sleep(2)

#Enter text into the Alert using send_keys()
obj.send_keys('krishna')

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

#Retrieve the message on the Alert window
message=obj.text
print ("Alert shows following message: "+ message )

time.sleep(2)

obj.accept()

#get the text returned when OK Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)
driver.save_screenshot("test.jpg")
driver.close