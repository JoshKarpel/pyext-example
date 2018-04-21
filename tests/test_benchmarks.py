import pytest

import time

from test import py_fizz_buzz_sum, numpy_fizz_buzz_sum, py_count_doubles, random_str
from example import fizz_buzz_sum, count_doubles


@pytest.mark.parametrize(
    'fn',
    (
        py_fizz_buzz_sum,
        numpy_fizz_buzz_sum,
        fizz_buzz_sum,
    )
)
def test_fizz_buzz_sum(benchmark, fn):
    result = benchmark(fn, 1000)

    assert result == 233168


@pytest.mark.parametrize(
    'fn',
    (
        py_count_doubles,
        count_doubles
    )
)
def test_count_doubles(benchmark, fn):
    str = random_str(1000)
    result = benchmark(fn, str)
