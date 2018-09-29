from test_framework import generic_test


def roman_to_integer(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s) - 1):
        if T[s[i]] < T[s[i + 1]]:
            result -= T[s[i]]
        else:
            result += T[s[i]]
    result += T[s[len(s) - 1]]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
