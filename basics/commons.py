from selenium import webdriver

driver_url="C:\Murali\Training\Selenium\chromedriver_win32\chromedriver.exe"
App_URL="http://localhost:8081/myapp/"
app_url = "http://localhost:8081/EmpDemo/"

def getChromeDriver():
    return  webdriver.Chrome(executable_path=driver_url)
"""

brower = webdriver.Firefox(executable_path ="C:\Murali\chromedriver.exe")

brower = webdriver.Ie(executable_path ="C:\Murali\chromedriver.exe")


"""