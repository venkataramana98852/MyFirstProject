import pytest

def test_first():
    print("Hello")

def test_second():
    a=10
    b=5
    assert (b+5) == a, "do not eqal" 
    print("true")

# @pytest.mark.skip
# @pytest.mark.smoke
@pytest.mark.xfail
def test_match():
    x="Hi"  
    assert x== "Hello" , "Not equal"   