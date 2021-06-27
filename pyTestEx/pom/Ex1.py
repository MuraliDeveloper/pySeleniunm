import pytest
from selenium.webdriver import Chrome
import time

from pom6.loginpage import loginpage
from util.commons import getChromeDriver


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver =  getChromeDriver()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def testloginwithemptyuername(browser):
    loginpageobj = loginpage(browser)
    loginpageobj.login("", "mahetha")
    alertObj = browser.switch_to.alert  # to get the alert obj
    msg = alertObj.text  # to get the alert msg
    assert "Please provide loginName!"== msg,"invalid msg for alert1"
    time.sleep(5)
    alertObj.accept()
    time.sleep(5)