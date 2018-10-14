from test_framework import generic_test, test_utils


def permutations(A):
    result, perm = [], [0]*len(A)

    def helper(n):
        if n == len(A):
            result.append(list(perm))
            return
        for c in A:
            if c not in perm[:n]:
                perm[n] = c
                helper(n + 1)

    helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
