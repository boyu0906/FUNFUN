from test_framework import generic_test, test_utils


def generate_power_set(S):
    def helper(input_set):
        if not input_set:
            return [[]]
        sub_result = helper(input_set[1:])
        return [s + [input_set[0]] for s in sub_result] + sub_result
    return helper(S)

    # def backtrack(a, k, A):
    #     if k == len(A):
    #         temp = []
    #         for i in range(len(A)):
    #             if a[i] == 1:
    #                 temp.append(A[i])
    #         result.append(temp)
    #     else:
    #         for c in [1, 0]:
    #             a[k] = c
    #             backtrack(a, k + 1, A)
    # result = []
    # a = [0] * len(S)
    # backtrack(a, 0, S)
    # return result

    # def helper(to_be_selected, selected_so_far):
    #     if to_be_selected == len(S):
    #         power_set.append(list(selected_so_far))
    #         return
    #     helper(to_be_selected + 1, selected_so_far)
    #     helper(to_be_selected + 1, selected_so_far + [S[to_be_selected]])
    # power_set = []
    # helper(0, [])
    # return power_set

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
