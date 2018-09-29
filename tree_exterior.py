import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right

    def left_exterior(node, is_boundary):
        if not node:
            return []
        if is_leaf(node):
            return [node]
        return ([node] if is_boundary else []) + left_exterior(node.left, is_boundary) + left_exterior(node.right, is_boundary and not node.left)

    def right_exterior(node, is_boundary):
        if not node:
            return []
        if is_leaf(node):
            return [node]
        return right_exterior(node.left, is_boundary and not node.right) + right_exterior(node.right, is_boundary) + ([node] if is_boundary else [])

    return [] if not tree else ([tree] + left_exterior(tree.left, True) + right_exterior(tree.right, True))


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
