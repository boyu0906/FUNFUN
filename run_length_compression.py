from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):  # '4a1b3c2a' --> 'aaaabcccaa'
    '''
    result = []
    i = 0
    while i < len(s):
        num = []
        while s[i].isdigit():
            num.append(s[i])
            i += 1
        result.append(s[i] * int(''.join(num)))
        i += 1
    return ''.join(result)
    '''
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)


def encoding(s):  # 'aaaabcccaa' --> '4a1b3c2a'
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
