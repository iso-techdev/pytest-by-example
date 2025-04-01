'''
Deferring the setup of parametrized resources (delay)
The parametrization of test functions happens at collection time. It is a good idea to setup expensive resources like 
DB connections or subprocess only when the actual test is run. Here is a simple example how you can achieve that. 
This test requires a db object fixture:

$ pytest tests/pkg4
or if your "cd tests"
$ pytest pkg4

'''
# content of test_backend.py

import pytest

def test_db_initialized(db):
    # a dummy test
    if(db.__class__.__name__ == "DB2"):
        pytest.fail("deliberately failing for demo purposes")



