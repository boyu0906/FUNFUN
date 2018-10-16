from test_framework import generic_test, test_utils


def combinations(n, k):
    if k == 0:
        return [[]]

    def helper(i, sub_set, candidates):
        if i == k:
            result.append(list(sub_set))   # list is needed!
            return
        for j in range(len(candidates)):
            sub_set[i] = candidates[j]
            curr_candidates = candidates[j + 1:]    # update candidates for the next round
            helper(i + 1, sub_set, curr_candidates)

    result, initial_set = [], [0]*k
    helper(0, initial_set, list(range(1, n + 1)))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
