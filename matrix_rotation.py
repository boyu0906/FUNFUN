from test_framework import generic_test


def rotate_matrix(square_matrix):
    num_layer = len(square_matrix) // 2
    matrix_size = len(square_matrix) - 1
    for i in range(num_layer):
        for j in range(i, matrix_size - i):
            (square_matrix[i][j], square_matrix[j][~i], square_matrix[~i][~j], square_matrix[~j][i]) = \
            (square_matrix[~j][i], square_matrix[i][j], square_matrix[j][~i], square_matrix[~i][~j])
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
