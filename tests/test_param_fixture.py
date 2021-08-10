import pytest
import os
 
@pytest.fixture(params=["mysql", "maria"])
def database(request):
    yield request.param
    
def test_somethingElse(database):
    assert 0 # for demo purpose
