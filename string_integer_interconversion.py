from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    if x == 0:
        return '0'
    is_negative = (x < 0)
    if is_negative:
        x = -x
    digits = []
    while x:  # cannot cover 0
        digits.append(chr(x % 10 + ord('0')))
        x = x // 10
    if is_negative:
        digits.append('-')

    return ''.join(reversed(digits))


def string_to_int(s):
    result = 0
    cnt = 0
    for i in reversed(range(len(s))):
        if s[i] != '-':
            result += (ord(s[i]) - ord('0')) * (10 ** cnt)
            cnt += 1
        else:
            result *= -1
            break
    return result


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
