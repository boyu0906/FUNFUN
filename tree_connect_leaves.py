import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def create_list_of_leaves(tree):

    def is_leaf(node):
        return not node.left and not node.right

    '''
    def helper(node):
        if node:
            if is_leaf(node):
                result.append(node)
            helper(node.left)
            helper(node.right)

    result = []
    helper(tree)
    return result
    '''

    def helper2(node):
        if not node:
            return []
        if is_leaf(node):
            return [node]
        return helper2(node.left) + helper2(node.right)

    return helper2(tree)


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure("Result list can't contain None")
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_connect_leaves.py",
                                       "tree_connect_leaves.tsv",
                                       create_list_of_leaves_wrapper))
