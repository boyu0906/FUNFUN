from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):

    spiral_result = []

    def perimeter_spiral(A):
        m = len(A)
        result = []
        for j in range(m):
            result.append(A[0][j])
        for i in range(1, m):
            result.append(A[i][m - 1])
        for j in reversed(range(0, m - 1)):
            result.append(A[m - 1][j])
        for i in reversed(range(1, m - 1)):
            result.append(A[i][0])
        return result

    cnt, n = 0, len(square_matrix)
    for k in range(n, 0, -2):
        temp = list([square_matrix[i][j] for j in range(cnt, n - cnt)] for i in range(cnt, n - cnt))
        spiral_result += perimeter_spiral(temp)
        cnt += 1
    return spiral_result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
