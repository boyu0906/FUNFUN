from test_framework import generic_test, test_utils


def generate_power_set(S):
    # def helper(input_set):
    #     if not input_set:
    #         return [[]]
    #     sub_result = helper(input_set[1:])
    #     return [s + [input_set[0]] for s in sub_result] + [s for s in sub_result]
    # return helper(S)

    def backtrack(a, k, A):
        if k == len(A):
            temp = []
            for i in range(len(A)):
                if a[i] == 1:
                    temp.append(A[i])
            result.append(temp)
        else:
            for c in [1, 0]:
                a[k] = c
                backtrack(a, k + 1, A)
    result = []
    a = [0] * len(S)
    backtrack(a, 0, S)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
