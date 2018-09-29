from test_framework import generic_test
from sorted_arrays_merge import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A):
    if len(A) < 2:
        return A
    B = []
    increase_flag, start = 1, 0
    for i in range(len(A) - 1):
        if increase_flag == 1:
            if A[i + 1] < A[i]:
                B.append(A[start:i+1])
                increase_flag, start = 0, i + 1
                continue
        if increase_flag == 0:
            if A[i + 1] > A[i]:
                B.append(list(reversed(A[start:i+1])))
                increase_flag, start = 1, i + 1
                continue
    if increase_flag == 1:
        B.append(A[start:])
    else:
        B.append(list(reversed(A[start:])))
    return merge_sorted_arrays(B)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
