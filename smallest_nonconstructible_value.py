from test_framework import generic_test



def smallest_nonconstructible_value(A):
    A.sort()
    if A[0] > 1:
        return 1
    partial_sum = 0
    for i, a in enumerate(A):
        if i == 0:
            partial_sum += a
        else:
            if a > partial_sum + 1:
                return partial_sum + 1
            else:
                partial_sum += a

    return partial_sum + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
