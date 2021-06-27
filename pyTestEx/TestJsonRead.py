import json
import time

import pytest
from basics import commons

CONFIG_PATH = 'Ex0/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

@pytest.fixture(scope='session')
def config():
  with open('data.json') as config_file:
    data = json.load(config_file)
  return data
"""
@pytest.fixture(scope='session')
def config_browser(config):
  if 'browser' not in config:
    raise Exception('The config file does not contain "browser"')
  elif config['browser'] not in ['chrome', 'firefox']:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  return config['browser']
  
@pytest.fixture(scope='session')
def config_wait_time(config):
  return config['wait_time'] if 'wait_time' in config else 10 
"""

@pytest.fixture
def browser(config):
  if config['browser'] == 'chrome':
    driver = commons.getChromeDriver()
  elif config['browser'] == 'firefox':
    driver = commons.getChromeDriver()
  else:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  driver.implicitly_wait(config['wait_time'])
  yield driver
  driver.quit()


def test_basic_duckduckgo_search(browser):
      # Set up some test case data
      URL = 'https://www.duckduckgo.com'
      PHRASE = 'panda'
      # Navigate to the DuckDuckGo home page
      browser.get(URL)
      time.sleep(5)
