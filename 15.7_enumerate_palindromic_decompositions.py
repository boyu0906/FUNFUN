from test_framework import generic_test


def palindrome_decompositions(input):
    def helper(S, partial):
        if len(''.join(partial)) == N:
            result.append(partial)
        for i in range(len(S)):
            if is_palindrom(S[:i+1]):
                helper(S[i+1:], partial + [S[:i+1]])

    def is_palindrom(S):
        return S == S[::-1]
    result = []
    N = len(input)
    helper(input, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
