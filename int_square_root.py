from test_framework import generic_test


def square_root(k):
    if 1 <= k <= 3:
        return 1
    L, U = 1, k // 2
    while L <= U:
        M = L + (U - L) // 2
        temp = M * M
        if temp == k:
            return M
        elif temp < k:
            L = M + 1
        else:
            U = M - 1

    return L-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
