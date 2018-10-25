from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    if k == 0:
        return 1
    result = [1, n] + [0] * (k - 1)
    for i in range(2, k + 1):
        if n - i <= k and result[n - i] != 0:
            result[i] = result[n - i]
        else:
            result[i] = result[i - 1] * (n - i + 1) / i
    return result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
