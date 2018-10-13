import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode


def reconstruct_preorder(preorder):
    if preorder == [None]:
        return None
    stack = []
    for i in reversed(range(len(preorder))):
        temp_data = preorder[i]
        if temp_data is not None:
            temp_node = BinaryTreeNode(temp_data, stack.pop(), stack.pop())
        else:
            temp_node = BinaryTreeNode(temp_data, None, None)
        stack.append(temp_node)
    return stack.pop()


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
