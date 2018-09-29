from test_framework import generic_test
import math


def square_root(x):
    left, right = (1.0, x) if x > 1.0 else (x, 1.0)
    #while (right - left >= 1e-11):
    while not math.isclose(left, right):
        middle = 0.5 * (left + right)
        temp = middle * middle
        if temp > x:
            right = middle
        else:
            left = middle
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
