from test_framework import generic_test


def is_well_formed(s):
    result = []
    pair = {'}': '{', ']': '[', ')': '('}
    for c in s:
        if c not in pair:
            result.append(c)
        elif not result or (pair[c] != result.pop()):
            return False

    return not result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
