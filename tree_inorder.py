from test_framework import generic_test


def inorder_traversal(tree):
    node_stack, result = [], []
    node = tree
    '''
    while node:
        node_stack.append(node)
        node = node.left
    while node_stack:
        top_node = node_stack.pop()
        result.append(top_node.data)
        # can be included in the first while loop
        if top_node.right:
            node_stack.append(top_node.right)
            temp_node = top_node.right.left
            while temp_node:
                node_stack.append(temp_node)
                temp_node = temp_node.left
    '''
    while node or node_stack:
        if node:
            node_stack.append(node)
            # going left
            node = node.left
        else:
            # going up
            top_node = node_stack.pop()
            result.append(top_node.data)
            # going right
            node = top_node.right

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
