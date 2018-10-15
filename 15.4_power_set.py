from test_framework import generic_test, test_utils


def generate_power_set(S):
    def helper(input_set):
        if not input_set:
            return [[]]
        sub_result = helper(input_set[1:])
        return [s + [input_set[0]] for s in sub_result] + [s for s in sub_result]
    return helper(S)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
