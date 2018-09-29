import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):

    # first step: remove 'b', forwards
    j, num_a = 0, 0
    for i in range(size):
        if s[i] != "b":
            s[j] = s[i]
            j += 1
        if s[i] == "a":
            num_a += 1

    # second step: replace each 'a' by two 'd's, backwards
    final_size = j + num_a
    k = final_size - 1
    for i in reversed(range(j)):
        if s[i] != "a":
            s[k] = s[i]
            k -= 1
        else:
            s[k] = s[k - 1] = "d"
            k -= 2

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
