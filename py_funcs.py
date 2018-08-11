import random
import string
import math

import numpy as np


def py_count_doubles(str):
    count = 0
    for a, b in zip(str, str[1:]):
        if a == b:
            count += 1

    return count


def random_str(length):
    return ''.join(random.choices(string.ascii_lowercase, k = length))


def py_fizz_buzz_sum(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)


def numpy_fizz_buzz_sum(limit):
    x = np.arange(1, limit, 1)
    return np.sum(np.where((x % 3 == 0) + (x % 5 == 0), x, 0))


def py_prime_factorization(n):
    factors = []
    n_sqrt = math.sqrt(n)

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    divisor = 3
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        elif divisor > n_sqrt:
            factors.append(n)
            break
        else:
            divisor += 2
    return factors
