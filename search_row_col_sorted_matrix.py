from test_framework import generic_test


def matrix_search(A, x):
    #if not A:
    #    return False
    num_row, num_col = len(A), len(A[0])
    row, col = 0, num_col - 1
    while row < num_row and col >= 0:
        if x > A[row][col]:
            row += 1
        elif x < A[row][col]:
            col -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
