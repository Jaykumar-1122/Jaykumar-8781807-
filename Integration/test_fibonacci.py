import pytest
from fibonacci import generate_fibonacci

def test_generate_fibonacci():
    assert generate_fibonacci(0) == [0]
    assert generate_fibonacci(1) == [0, 1, 1]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3, 5]
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_large_limit():
    assert generate_fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_generate_fibonacci_negative_limit():
    with pytest.raises(ValueError):
        generate_fibonacci(-10)
