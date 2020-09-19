from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:\Murali\Mythri Progs\selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("")

"""
<!DOCTYPE html> <html> <frameset rows="*,*,*,*"> <frame src="frame_1.html"> <frame src="frame_2.html"> <frame src="frame_3.html"> <frame src="frame_4.html"> </frameset> </html>
 
 or
 
 <frameset rows="150px,*">
    <frame noresize src="frame_1.html">
    <frameset cols="20%,*,20%">
        <frame src="frame_2.html">
        <frame src="frame_3.html">
        <frame src="frame_4.html">
    </frameset>
</frameset>


Read more: https://html.com/frames/#ixzz6SIP8NvjP
 
 
"""
#switch to frame by id name or id or index
driver.switch_to.frame("frameaname1")# id or index can be passed

#perform all actvities on this frame

driver.switch_to.default_content()#switch to main page
driver.switch_to.frame("frameaname2")

#perform all actvities on this frame

driver.switch_to.default_content()
driver.switch_to.frame("frameaname3")

#perform all actvities on this frame




driver.close 