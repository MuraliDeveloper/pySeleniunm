

"""
<!DOCTYPE html> <html> <frameset rows="*,*,*,*"> <frame src="frame_1.html"> <frame src="frame_2.html"> <frame src="frame_3.html"> <frame src="frame_4.html"> </frameset> </html>
 
 or
 frames.html:
-----------------------------------------------
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>


 <frameset rows="150px,*">
    <frame noresize src="frame_1.html">
    <frameset cols="20%,*,20%">
        <frame src="frame_2.html">
        <frame src="frame_3.html">
        <frame src="frame_4.html">
    </frameset>
</frameset>


</body>
</html>



frame_1.html:
-----------------
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

 Enter name: <input type="text" name="data1"/>


</body>
</html>


frame_2.html:
--------------------
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

Enter Lname: <input type="text" name="data2"/>

</body>
</html>

frame_3.html:
--------------------
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

Enter Surname: <input type="text" name="data3"/>

</body>
</html>


frame_4.html:
--------------------

<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

Enter city: <input type="text" name="data4"/>

</body>
</html>



frames.html:
---------------------------------
<iframe name="frame1" src="frame_1.html"></iframe>
<iframe name="frame2" src="frame_2.html"></iframe>
<iframe name="frame3" src="frame_3.html"></iframe>
<iframe name="frame4" src=frame_4.html></iframe>


 
 How to switch to a frame?
 	   1.driver.switch_to.frame(<num>);
      ex:
        driver.switch_to.frame(1);
       
     2.driver.switch_to.frame("<id>");
     ex:
	   driver.switch_to.frame("fr1");

How to switch to a parent frame?	
       driver.switch_to.default_content()  
	  
	 driver.switchTo().parentFrame();
 
"""

from selenium import webdriver

from basics import commons

import time
driver = commons.getChromeDriver()
driver.maximize_window()
driver.get("")


driver.switch_to.frame("fr1")
driver.find_element_by_name("data1").send_keys("kumar")
time.sleep(3)

driver.switch_to.default_content()#switch to main page

driver.switch_to.frame("fr2")
driver.find_element_by_name("data2").send_keys("varma")
time.sleep(3)

driver.switch_to.default_content()#switch to main page

driver.switch_to.frame("fr3")
driver.find_element_by_name("data3").send_keys("ramesh")
time.sleep(3)

driver.switch_to.default_content()#switch to main page

driver.switch_to.frame("fr4")
driver.find_element_by_name("data4").send_keys("suresh")
time.sleep(3)

driver.switch_to.default_content()#switch to main page
driver.find_element_by_name("id").send_keys("1313131")


driver.close()