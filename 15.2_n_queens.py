from test_framework import generic_test


def n_queens(n):
    result, col_pos = [], [0]*n

    def n_queens_helper(row):
        if row == n:
            result.append(list(col_pos))
            return
        for col in range(n):
            if all(abs(col - c) not in (0, row - i) for i, c in enumerate(col_pos[:row])):
                col_pos[row] = col
                n_queens_helper(row + 1)

    n_queens_helper(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
