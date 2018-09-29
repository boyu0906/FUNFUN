from test_framework import generic_test


def is_symmetric(tree):
    def test_symmetric(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2:
            if tree1.data == tree2.data:
                return test_symmetric(tree1.left, tree2.right) and test_symmetric(tree1.right, tree2.left)
        return False
    if not tree:
        return True
    return test_symmetric(tree.left, tree.right)

    ''' 
    def test_symmetric(tree1, tree2):
        if not tree1.left and not tree1.right and not tree2.left and not tree2.right:
            return True
        if tree1.left and not tree2.right or tree2.right and not tree1.left:
            return False
        if tree1.right and not tree2.left or tree2.left and not tree1.right:
            return False
        result1 = result2 = True
        if tree1.left and tree2.right:
            if tree1.left.data == tree2.right.data:
                result1 = test_symmetric(tree1.left, tree2.right)
            else:
                return False
        if tree1.right and tree2.left:
            if tree1.right.data == tree2.left.data:
                result2 = test_symmetric(tree1.right, tree2.left)
            else:
                return False
        return result1 and result2

    if not tree or (not tree.left and not tree.right):
        return True
    if tree.left and tree.right and tree.left.data == tree.right.data:
        result = test_symmetric(tree.left, tree.right)
        return result
    else:
        return False
    '''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
