'''
Profiling test duration
If you have a slow running large test suite you might want to find out which tests are the slowest. Let’s make an artificial test suite:
$pytest ./tests/test_some_are_slow.py --durations=3
'''
# content of test_some_are_slow.py
import time

def test_funcfast():
    time.sleep(0.1)


def test_funcslow1():
    time.sleep(0.2)

def test_funcslow2():
    time.sleep(0.3)
