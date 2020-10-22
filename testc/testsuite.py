import pytest, sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


from  mathmod.mathclass import MathClass

@pytest.fixture
def math_class():
    return MathClass()

# test for initialization
def test_init(math_class):
    assert math_class.num == 0

# test for factorial calculation
def test_factorial(math_class):
    assert math_class.factorial(5) == 120

def test_factorial1(math_class):
    assert math_class.factorial(-1) == 0

def test_factorial3(math_class):
    assert math_class.factorial(1) == 1

@pytest.mark.parametrize("n1,n2", [
    (2,2),
    (2,2),
])
def test_scenarios(n1, n2,math_class):
    fact = math_class.factorial(n1)
    square = math_class.square(n2)
    assert fact == square - 2


def test_add10(math_class):
    n = math_class.add10(10)
    assert n  == 20

def test_sub10(math_class):
    n = math_class.sub10(30)
    assert n  == 20
