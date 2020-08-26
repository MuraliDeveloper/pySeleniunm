from selenium import webdriver
import time

"""
<!DOCTYPE html>
<html>
<body bgcolor="#C0C0C0">
<h1>
Simple Alert Demonstration</h1>
<p>
click the Below Button to create an Alert</p>
<button onclick="alertFunction()" name ="alert"> Create Alert</button>
<script>
function alertFunction() {
 alert("Hi!, I am a Simple Alert. Please Click on the 'OK' Button.");
}
</script>
</body>
</html>
"""

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("")

#Click on the "Alert" button to generate the Simple Alert
button = driver.find_element_by_name('alert')
button.click()
#Switch the control to the Alert window
obj = driver.switch_to.alert
# or driver.switch_to_alert().accept()
# or driver.switch_to_alert().dismiss()

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )
time.sleep(2)

#use the accept() method to accept the alert
obj.accept()
print(" Clicked on the OK Button in the Alert Window")
driver.close 