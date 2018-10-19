from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    def helper(left, right, partial):
        if left == right == 0:
            result.append(partial)
            return
        if left > 0:
            helper(left - 1, right, partial + '(')
        if left < right:
            helper(left, right - 1, partial + ')')
    result = []
    helper(num_pairs, num_pairs, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
