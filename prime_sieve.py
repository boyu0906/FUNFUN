from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    if n < 2:
        return []
    # if n == 2:
    #     return [2]

    primes = [2]
    K = (n - 3) // 2 + 1  # number of odd numbers up to and including n
    is_prime = [True] * K
    # num: 3 5 7 9 11 ...
    #   k: 0 1 2 3 4  ...
    for k in range(K):
        if is_prime[k]:
            for i in range(2 * k**2 + 6 * k + 3, K, 2 * k + 3): # need to be very careful about the range
                is_prime[i] = False
            primes.append(2*k+3)

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
