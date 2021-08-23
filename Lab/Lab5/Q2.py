def tree_search(target, node):
    if node == None:
        return False
    if node.value == target:
        return True
    if node.value < target:
        return tree_search(target, node.right)
    else:
        return tree_search(target, node.left)
