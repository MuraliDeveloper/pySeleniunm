

from util.commons import getChromeDriver
import time

def test_add_5():
    driver = getChromeDriver()
    driver.get("https://www.gmail.com")
    time.sleep(3)


