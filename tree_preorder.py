from test_framework import generic_test


def preorder_traversal(tree):

    '''
    node_stack, result = [], []
    node = tree
    while node:
        result.append(node.data)
        if node.right:
            node_stack.append(node.right)
        node = node.left
    while node_stack:
        top_node = node_stack.pop()
        result.append(top_node.data)
        if top_node.right:
            node_stack.append(top_node.right)
        temp = top_node.left

        while temp:
            result.append(temp.data)
            if temp.right:
                node_stack.append(temp.right)
            temp = temp.left
    '''
    if not tree:
        return []
    node_stack, result = [tree], []
    while node_stack:
        top_node = node_stack.pop()
        result.append(top_node.data)
        if top_node.right:
            node_stack.append(top_node.right)
        if top_node.left:
            node_stack.append(top_node.left)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
