from selenium import webdriver

driver_url="C:\Murali\Training\Selenium\chromedriver_win32\chromedriver.exe"
app_url="http://localhost:8080/testFb/"
App_URL="http://localhost:8080/testFb/"


def getChromeDriver():
    return  webdriver.Chrome(executable_path=driver_url)
"""

brower = webdriver.Firefox(executable_path ="C:\Murali\chromedriver.exe")

brower = webdriver.Ie(executable_path ="C:\Murali\chromedriver.exe")


"""