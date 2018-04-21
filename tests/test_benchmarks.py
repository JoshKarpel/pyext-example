import pytest

import time

from test import py_fizz_buzz_sum, numpy_fizz_buzz_sum, py_count_doubles, py_prime_factorization, random_str
from example import fizz_buzz_sum, count_doubles, prime_factorization


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
        count_doubles,
    )
)
def test_count_doubles(benchmark, fn):
    str = random_str(1000)
    result = benchmark(fn, str)


@pytest.mark.parametrize(
    'fn',
    (
        py_prime_factorization,
        prime_factorization,
    )
)
def test_prime_factorization_composite(benchmark, fn):
    n = 1231564617245714
    result = benchmark(fn, n)

    target = [2, 17, 17, 17, 29, 31, 61, 2285551]
    assert result == target


@pytest.mark.parametrize(
    'fn',
    (
        py_prime_factorization,
        prime_factorization,
    )
)
def test_prime_factorization_on_prime(benchmark, fn):
    n = 275604547
    result = benchmark(fn, n)

    target = [275604547]
    assert result == target
