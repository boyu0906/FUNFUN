from test_framework import generic_test


def longest_contained_range(A):
    S = set(A)
    max_length = 0
    while S:
        a = S.pop()
        cnt = 1
        temp = a + 1
        while temp in S:
            S.remove(temp)
            temp += 1
            cnt += 1
        temp = a - 1
        while temp in S:
            S.remove(temp)
            temp -= 1
            cnt += 1
        max_length = max(max_length, cnt)

    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
