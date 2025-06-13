# pytest-example
pytest - Python Testing Example

This is a simple example of how to use pytest to integreate testing in your Python application.
It contains project structure 


## Usage 
pytest -v

-v for increase the output ( verbose)




## Code Structure

```
src/pytest_by_example/
    pkg1
     __init__.py
     addition.py
     multiplication.py
    pkg2/
        __init__.py
        myclass.py
    __init__.py
    main.py
tests/
    __init__.py
    pkg1
    pkg2
    ..
    ..
    test_multiplication.py
    test_some_are_slow.py
       
```

## Instructions
# YOU NEED TO FIX THE FAILED UNIT TESTS
1- Read and understand the pytest.ini file under the root of this project. This files is triggered and read as a configuration file by "pytest" before an test execution
2- You need to go through all test and execute them and fix the unit tests which are failed 
3- To isolate and run any test module ( python file) go to the root folder 

```
 $ pwd 
```
~/workspace/workspace-python/pytest-by-example   ( on my GitBash window)

For example I want to execute only the python module  
 tests/pkg1/addition.py to test the addition method which I have inside the src/pk1/addition.py module or python file 

 ```
  $  pytest tests/pkg1/test_addition.py 
 ```

For example I want to test the unit tests module ( python file) called  test_multiplication.py  also I want to increase the debug ( verbose )

 ```
  $   pytest  -v tests/test_multiplciation.py

 ```

# Before you fix the unit test, you need to go through the code and understand all the code in the project after that you run individual module (python file) to see and watch 
# Try to change things to understand more  

## Contribute
Please contribute with different cases to help the python community with pytest more examples 
