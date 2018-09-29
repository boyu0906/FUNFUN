from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    ind1, ind2, ind3 = m - 1, n - 1, m + n - 1
    '''
    while ind3 >= 0:
        if ind1 < 0:
            A[ind3] = B[ind2]
            ind2 -= 1
        elif ind2 < 0:
            A[ind3] = A[ind1]
            ind1 -= 1
        else:
            if A[ind1] > B[ind2]:
                A[ind3] = A[ind1]
                ind1 -= 1
            else:
                A[ind3] = B[ind2]
                ind2 -= 1
        ind3 -= 1
    '''
    while ind1 >= 0 and ind2 >= 0:
        if A[ind1] > B[ind2]:
            A[ind3] = A[ind1]
            ind1 -= 1
        else:
            A[ind3] = B[ind2]
            ind2 -= 1
        ind3 -= 1
    while ind2 >= 0:
        A[ind3] = B[ind2]
        ind2, ind3 = ind2 - 1, ind3 - 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
