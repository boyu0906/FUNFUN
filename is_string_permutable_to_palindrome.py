from test_framework import generic_test
import collections


def can_form_palindrome(s):
    C = collections.Counter(s)
    ''''
    tot = 0
    for num in C.values():
        if num % 2:
            tot += 1
    '''
    tot = sum(num % 2 for num in C.values())
    return tot <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
