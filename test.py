import example
import numpy as np
import random
import string

# print(example.__dict__.items())
for k, v in example.__dict__.items():
    print(k, '-->', v)
print()


def py_count_doubles(str):
    count = 0
    for a, b in zip(str, str[1:]):
        if a == b:
            count += 1

    return count


def random_str(length = 100):
    return ''.join(random.choices(string.ascii_lowercase, k = length))


str = random_str(1000)
print(example.count_doubles(str))
print(py_count_doubles(str))


def py_fizz_buzz_sum(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)


def numpy_fizz_buzz_sum(limit):
    x = np.arange(1, limit, 1)
    return np.sum(np.where((x % 3 == 0) + (x % 5 == 0), x, 0))


print(example.fizz_buzz_sum(1000))
print(py_fizz_buzz_sum(1000))
print(numpy_fizz_buzz_sum(1000))
