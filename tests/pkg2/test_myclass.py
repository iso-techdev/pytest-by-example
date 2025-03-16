from pytest_by_example.pkg2.myclass import MyClass

import pytest
import os

'''
We are trying to show the data loading which is needed for a given file to test 
we have the data folder under the root folder of the project 
'''
@pytest.fixture
def root_dir():
    # this is the current directory which is../tests/pkg2
    return os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def data_dir(root_dir):
    # print(root_dir) print statement  works 
    return root_dir + "/../../data/"


def test_load_file_from_fixture(data_dir):
    # print(data_dir) 
    with open(data_dir + '/gnews/GoogleNews.txt') as my_data_file:
        data = my_data_file.readlines()
        assert data != None

    #assert 0  # to see what was printed above or on the command line pytest  -s 
        
def test_myclass_result():
    myclass = MyClass()
    assert "OK" != myclass.get_result()
