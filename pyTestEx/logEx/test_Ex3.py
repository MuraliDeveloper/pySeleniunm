
"""
run using :

1.pytest test_Ex3.py
2.pytest --capture=no test_Ex3.py
3.pytest -s test_Ex3.py


pytest.ini:
-------------------------
console output

[pytest]
log_cli = 1
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
log_cli_date_format=%Y-%m-%d %H:%M:%S


OR
file output

[pytest]
log_file = pytest.log
log_file_level = 1
log_file_format = "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
log_file_date_format = "%Y-%m-%d %H:%M:%S"

"""

import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

def test_1():
    LOGGER.info('test_1 started')
    LOGGER.debug('test_1 critical')
    assert True

def test_2():
    LOGGER.info('test_2 started')
    LOGGER.debug('test_2 critical')
    assert False