import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    '''
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(-1, -1)
    left, n, remaining_to_cover = 0, len(keywords), len(keywords)

    for right, word in enumerate(paragraph):
        if word in keywords:
            keywords_to_cover[word] -= 1
            if keywords_to_cover[word] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == Subarray(-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
                if right - left == n - 1:
                    return result
            if paragraph[left] in keywords:
                keywords_to_cover[paragraph[left]] += 1
                if keywords_to_cover[paragraph[left]] > 0:
                    remaining_to_cover += 1
            left += 1
    return result
    '''

    table, dist = {}, float('inf')
    n = len(keywords)
    for i, x in enumerate(paragraph):
        if x in keywords:
            table[x] = i
        if len(table) == n:
            min_ind_temp = min(table.values())
            max_ind_temp = max(table.values())
            dist_temp = max_ind_temp - min_ind_temp
            if dist_temp < dist:
                dist = dist_temp
                min_ind = min_ind_temp
                max_ind = max_ind_temp
                if dist_temp == n - 1:
                    return Subarray(min_ind, max_ind)
    return Subarray(min_ind, max_ind)



@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
