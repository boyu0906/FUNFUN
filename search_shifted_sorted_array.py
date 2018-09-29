from test_framework import generic_test


def search_smallest(A):
    #if len(A) == 1:
    #    return 0
    L, U = 0, len(A) - 1
    while L < U:
        M = L + (U - L) // 2
        if A[M] < A[U]:
            U = M
        else:
            L = M + 1
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
