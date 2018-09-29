from test_framework import generic_test


def rabin_karp(t, s):
    m, n = len(s), len(t)
    for i in range(n - m + 1):
        if t[i:i + m] == s:
            return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
