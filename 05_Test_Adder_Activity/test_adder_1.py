import adder

def test_adder_case_1():
    """Testing adding 2 and 3"""
    number = adder.add(2,3)
    assert number == 5 

def test_adder_case_2():
    number = adder.add(4,5)
    assert number == 9