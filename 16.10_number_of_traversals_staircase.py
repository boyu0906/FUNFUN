from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    num_ways = [1] + [0] * top
    for i in range(1, top + 1):
        for j in range(1, min(maximum_step,i) + 1):
            num_ways[i] += num_ways[i - j]
    return num_ways[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
