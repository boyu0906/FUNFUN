from test_framework import generic_test


def binary_tree_depth_order(tree):
    if not tree:
        return []
    result = []
    node_depth_iter = [tree]
    while node_depth_iter:
        '''
        temp1, temp2 = [], []
        for node in node_depth_iter:
            temp1.append(node.data)
            if node.left:
                temp2.append(node.left)
            if node.right:
                temp2.append(node.right)
        result.append(temp1)
        node_depth_iter = temp2
        '''
        result.append([node.data for node in node_depth_iter])
        node_depth_iter = [child for node in node_depth_iter for child in (node.left, node.right) if child]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
