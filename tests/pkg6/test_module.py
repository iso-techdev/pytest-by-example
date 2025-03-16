'''
test classes may now define a callme method which will be called ahead of running any tests:
$ pytest tests/pkg6 -s   
-s to show the stdout or print statement 
'''
# content of test_module.py

class TestHello:
    # called before running any test cases in  this class
    @classmethod
    def callme(cls):
        print(f"callme called! from {cls.__name__}")

    def test_method1(self):
        print("test_method1 called")

    def test_method2(self):
        print("test_method2 called")
    

class TestOther:
    # called before running any test cases in  this class
    @classmethod
    def callme(cls):
        print(f"callme called from {cls.__name__}")

    def test_other(self):
        print("test other")

# works with unittest as well ...
import unittest

class SomeTest(unittest.TestCase):
    # called before running any test cases in  this class
    @classmethod
    def callme(cls):
        print(f"callme called from {cls.__name__}")

    def test_unit1(self):
        print("test_uit1 method called")

