'''
A session-scoped fixture effectively has access to all collected test items. 
Here is an example of a fixture function which walks all collected tests and looks if their test class defines a callme method and calls it:

'''

# content of conftest.py

import pytest

@pytest.fixture(scope="session",autouse=True)
def callattr_ahead_of_alltests(request):
    print("callattr_ahead_of_alltets called")
    seen = {None}
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj,"callme"):
                cls.obj.callme()
        seen.add(cls)    