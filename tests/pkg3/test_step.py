# content of test_step.py
'''
We’ll see that test_deletion was not executed because test_modification failed. It is reported as an “expected failure”.

$ pytest -rx  pkg3 
target all test module in pkg3 which will pick up the conftest.py 
It is discourage to add conftest.py in the root folder since it slow the tests and each module will try to pick it up so be specific
inside which package you want to add contest.py
'''
import pytest

@pytest.mark.incremental
class TestUserHandling:
    def test_login(self):
        pass
    
    def test_modification(self):
        assert 0

    def test_deletion(self):
        pass 

def test_normal():
    pass
