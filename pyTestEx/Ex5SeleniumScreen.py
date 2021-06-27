from pytest_html_reporter import attach

from util.commons import getChromeDriver
import time

def test_add_5():
    driver = getChromeDriver()
    driver.get("https://www.gmail.com")
    time.sleep(3)
    attach(data=driver.get_screenshot_as_png())
    driver.quit()