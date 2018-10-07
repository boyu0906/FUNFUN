from test_framework import generic_test
from binary_tree_node import BinaryTreeNode



def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None
    '''
    root = preorder_sequence[0]
    left_seq, right_seq = [], []
    left_seq = [x for x in preorder_sequence if x < root]
    right_seq = [x for x in preorder_sequence if x > root]
    return BinaryTreeNode(root, rebuild_bst_from_preorder(left_seq), rebuild_bst_from_preorder(right_seq))
    '''

    transition_point = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))

    return BinaryTreeNode(preorder_sequence[0], rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
                          rebuild_bst_from_preorder(preorder_sequence[transition_point:]))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
