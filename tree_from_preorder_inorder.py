from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    if not preorder:
        return None

    k = 0
    for i in inorder:
        if i != preorder[0]:
            k += 1
        else:
            break
    inorder_left = inorder[0:k]
    inorder_right = inorder[k+1:]
    preorder_left = preorder[1:k+1]
    preorder_right = preorder[k+1:]

    root_left = binary_tree_from_preorder_inorder(preorder_left, inorder_left)
    root_right = binary_tree_from_preorder_inorder(preorder_right, inorder_right)

    return BinaryTreeNode(preorder[0], root_left, root_right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
