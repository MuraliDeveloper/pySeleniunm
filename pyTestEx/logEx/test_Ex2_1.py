"""
run using :
1.pytest test_Ex2.py
2.pytest --capture=no test_Ex2.py

"""
import logging

LOGGER = logging.getLogger(__name__)

def test_1():
    LOGGER.info('test started')
    LOGGER.warning('test running')
    LOGGER.error('test error')
    LOGGER.critical('test critical')
    LOGGER.debug("checking")
    assert 1==1, "success"