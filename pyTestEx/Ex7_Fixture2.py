
"""
WebDriver setup is best handled using a pytest fixture.

Any test requiring a WebDriver instance can simply call the fixture to get it.

browser is a pytest fixture function, as denoted by the @pytest.fixture decorator.
Let’s step through each line to understand what this new fixture does.

"""


from util.commons import getChromeDriver
import pytest
import time


@pytest.fixture
def browser():
  driver = getChromeDriver()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_Google(browser):
      URL = 'https://www.google.com'
      browser.get(URL)
      time.sleep(5)

def test_fb(browser):
    URL = 'https://www.fb.com'
    browser.get(URL)
    time.sleep(5)
