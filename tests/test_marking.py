import pytest
 
@pytest.mark.dicttest("This is dicttest")
def test_dicttest_1():
    assert True

@pytest.mark.dicttest("This is dicttest")
def test_dicttest_2():
    assert True

@pytest.mark.listtest("This is listtest")
def test_listtest1():
    assert True

@pytest.mark.listtest("This is listtest")
def test_listtest2():
    assert True

def test_somethingelse():
    assert False