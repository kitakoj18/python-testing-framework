from python_testing_framework import increment
import pytest

def test_zero():
  assert increment.zero() == 0

@pytest.mark.parametrize('test_input, expected', [(-1, 0), (2, 3), (21, 22), (102, 103), (1001, 1002)])

def test_inc(test_input, expected):
    assert increment.inc(test_input) == expected

def test_inc_error():
    with pytest.raises(TypeError):
        increment.inc('hello!')

@pytest.fixture
def test_values():
    return {'i': 2, 'j': 200, 'k': 2000}

def test_zero_dict_values(test_values):
    increment.zero_dict_values(test_values)
    assert test_values == {'i': 0, 'j': 0, 'k': 0}

def test_inc_dict_values(test_values):
    increment.inc_dict_values(test_values)
    assert test_values == {'i': 3, 'j': 201, 'k': 2001}
