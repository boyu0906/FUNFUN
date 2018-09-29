from test_framework import generic_test


def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i].isalnum() and s[j].isalnum():
            if s[i].lower() == s[j].lower():
                i, j = i + 1, j - 1
            else:
                return False
        while not s[i].isalnum() and i < j:  # use while instead of if can be more efficient!!!
            i += 1
        while not s[j].isalnum() and i < j:  # use while instead of if can be more efficient!!!
            j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
