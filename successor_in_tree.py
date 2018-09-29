import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node):
    if node.right:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp
    else:
        if not node.parent:
            return None
        elif node == node.parent.left:
            return node.parent
        else:
            temp = node.parent
            while temp.left != node:
                node = temp
                temp = temp.parent
                if not temp:
                    return None
            return temp


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("successor_in_tree.py",
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
