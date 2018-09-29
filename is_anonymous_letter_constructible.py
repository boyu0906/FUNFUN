from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    C1 = collections.Counter(letter_text)

    for c in magazine_text:
        if c in letter_text:
            C1[c] -= 1
            if C1[c] <= 0:
                del C1[c]
                if not C1:
                    return True
        #print(c, C1)
    '''
    C2 = collections.Counter(magazine_text)
    for x in C1:
        if C1[x] > C2[x]:
            return False
    '''
    return not C1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
