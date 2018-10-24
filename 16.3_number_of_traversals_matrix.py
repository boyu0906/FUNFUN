from test_framework import generic_test


def number_of_ways(n, m):
    num_ways = [[0]*m for _ in range(n)]
    for i in range(m):
        num_ways[0][i] = 1
    for j in range(n):
        num_ways[j][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            num_ways[i][j] = num_ways[i][j - 1] + num_ways[i - 1][j]
    return num_ways[n - 1][m - 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
