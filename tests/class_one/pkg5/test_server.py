'''
Marking test functions and selecting them for a run
You can “mark” a test function with custom metadata like this:
$ pytest -v -m "device(serial='123')"
$ pytest -v -m "not webtest"   (negate)  
'''
# content of test_server.py

import pytest

@pytest.mark.webtest
def test_send_http():
    pass # perform sone webtest test for your app

@pytest.mark.device(serial="123")
def test_something_quick():
    pass

@pytest.mark.device(serial="abd")
def test_another():
    pass


class TestClass:
    def test_method(self):
        pass