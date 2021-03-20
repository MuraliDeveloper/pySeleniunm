
"""
run using :
1.pytest test_Ex2.py
2.pytest --capture=no test_Ex2.py

"""
def test_1():
    print('test_1 started')
    print('test_1 critical')
    assert 1==1 , "success"

def test_2():
    print('test_2 started')
    print('test_2 critical')
    assert 1==0 ,"failure"