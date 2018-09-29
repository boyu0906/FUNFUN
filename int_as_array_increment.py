from test_framework import generic_test


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        # in case such as 99 + 1 = 100, there is a carry-out
        # a slick way to do this is to append 0 at the end,
        # and update the first entry to 1
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
