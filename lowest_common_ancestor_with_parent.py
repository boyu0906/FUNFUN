import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth
    depth0, depth1 = get_depth(node0), get_depth(node1)
    '''
    temp = node0
    while temp:
        depth0 += 1
        temp = temp.parent
    temp = node1
    while temp:
        depth1 += 1
        temp = temp.parent
    '''
    # make node0 as the deeper node in order to simplify the code
    if depth1 > depth0:
        node0, node1 = node1, node0
    delta = abs(depth1 - depth0)
    while delta:
        node0 = node0.parent
        delta -= 1
    '''
    delta = depth0 - depth1
    if delta > 0:
        k = delta
        while k:
            node0 = node0.parent
            k -= 1
    else:
        k = -delta
        while k:
            node1 = node1.parent
            k -= 1
    '''

    while node0:
        if node0 == node1:
            return node0
        node0, node1 = node0.parent, node1.parent

    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
