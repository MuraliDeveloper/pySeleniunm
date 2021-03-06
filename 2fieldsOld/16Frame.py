from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("")

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


"""
#switch to frame by id name or id or index
driver.switch_to.frame("frame1")# id or index can be passed

#perform all actvities on this frame

driver.switch_to.default_content()#switch to main page
driver.switch_to.frame("frame2")

#perform all actvities on this frame

driver.switch_to.default_content()
driver.switch_to.frame("frame3")

#perform all actvities on this frame


driver.close 