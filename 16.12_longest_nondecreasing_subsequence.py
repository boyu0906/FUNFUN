from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    longest_length = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] >= A[j]:
                longest_length[i] = max(longest_length[i], longest_length[j] + 1)
    return max(longest_length)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
