from test_framework import generic_test


def apply_permutation(perm, A):
    N = len(A)
    for i in range(N):
        next_i = i
        while perm[next_i] >= 0:
            A[i], A[perm[next_i]] = A[perm[next_i]], A[i]
            temp = perm[next_i]
            perm[next_i] -= N
            next_i = temp
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
