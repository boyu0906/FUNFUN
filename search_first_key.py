from test_framework import generic_test


def search_first_of_k(A, k):
    L, U = 0, len(A) - 1

    while L <= U:
        M = L + (U - L) // 2
        if A[M] == k:
            if M >= 1 and A[M - 1] == k:
                U = M - 1
            else:
                return M
        elif A[M] < k:
            L = M + 1
        else:
            U = M - 1
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
