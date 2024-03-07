import pytest
from ukp_github import Fibonacci


# This is a test function
def test_import():
    # This checks __init__ was set up correctly
    try:
        from ukp_github import Fibonacci
    except ImportError:
        assert False


def test_fib():
    fibonacci = Fibonacci()
    assert fibonacci.fib(10) == 55
