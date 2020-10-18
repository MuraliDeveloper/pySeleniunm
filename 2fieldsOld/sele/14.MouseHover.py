#!/usr / bin / env python
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# set webdriver path here it may vary
driver = webdriver.Chrome(executable_path="C:\Murali\Training\chromedriver_win32\chromedriver.exe")

"""
How to move mouse over element?
use action obj to move the mouse over element


action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_id("mylabel")
action.move_to_element(firstLevelMenu).perform()


<script>
function bigImg(x) {
  x.style.height = "64px";
  x.style.width = "64px";
}

function normalImg(x) {
  x.style.height = "32px";
  x.style.width = "32px";
}
</script>

<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("p").mouseover(function(){
    $("p").css("background-color", "yellow");
  });
  $("p").mouseout(function(){
    $("p").css("background-color", "lightgray");
  });
});
</script>
</head>
<body>

<img onmouseover="bigImg(this)" onmouseout="normalImg(this)" border="0" 
src="mypic.gif" alt="Smiley" width="32" height="32">



<br/><br/>
<p id="mylabel">Move the mouse pointer over this paragraph.</p>

enter name :
<input type="text" name="name" />
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
Enter the data :  <input type="text" id="data" />
</body>
</html>

"""



driver.get("https://UrlToOpen")
"""
1.create action object and perform mouse operations using this obj 
"""
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_id("mylabel")
action.move_to_element(firstLevelMenu).perform()
time.sleep(5)

"""
1.enter selenium text for the text field 
find element
move the mouse over the element
click on element
enter selenium

"""
textField = driver.find_element_by_name("name")
action.move_to_element(textField)
time.sleep(5)
action.click()
time.sleep(5)
action.send_keys_to_element(textField,"selenium")
time.sleep(5)
action.double_click(textField)
time.sleep(5)
action.context_click(textField)
time.sleep(5)
action.perform()


action.move_to_element(textField).click().send_keys_to_element(textField,"selenium").double_click(textField).context_click(textField).perform()

"""
scroll to the element
"""
driver = webdriver.Chrome()
driver.get('')
target = driver.find_element_by_name('data')
driver.execute_script('arguments[0].scrollIntoView(true);', target)
time.sleep(5)




