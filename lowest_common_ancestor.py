import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import namedtuple



def lca(tree, node0, node1):
    Status = namedtuple('Status', ('num', 'ancestor'))
    def check(tree, node0, node1):
        if not tree:
            return Status(0, None)
        left_result = check(tree.left, node0, node1)
        if left_result.num == 2:
            return left_result
        right_result = check(tree.right, node0, node1)
        if right_result.num == 2:
            return right_result
        temp = left_result.num + right_result.num + ((node0, node1).count(tree))
        return Status(temp, tree if temp == 2 else None)

    return check(tree, node0, node1).ancestor

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
