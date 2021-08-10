import pytest
import os
 
@pytest.fixture(autouse=True)
def change_user_env():
    # before
    curuser = os.environ.get("USER")
    os.environ["USER"] = "foobar"
    yield
    
    # after
    os.environ["USER"] = curuser


def test_somethingelse():
    assert os.getenv("USER") == "foobar"