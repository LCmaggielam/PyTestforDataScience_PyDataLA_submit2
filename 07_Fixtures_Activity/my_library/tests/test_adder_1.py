"""Add tests for adders here """
import pytest
from .. import my_module


@pytest.fixture(scope="session")
def adder_fixture():
    adder = my_module.SingleObject(5)
    return adder

def test_add_5(adder_fixture):
    total = adder_fixture.add_more(5)
    assert total == 10

def test_add_6(adder_fixture):
    total = adder_fixture.add_more(6)
    assert total == 11


