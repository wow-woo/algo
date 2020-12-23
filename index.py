def traverseTree(tree, target, closest, n):
    if not tree:
        return
    diff_l = n_l = diff_r = n_r = float('inf')

    diff = abs(tree.value - target)
    if diff < closest:
        closest = diff
        n = tree.value

    if tree.value > target:
        # make tree.value smaller
        if tree.left:
            diff_l, n_l = traverseTree(tree.left, target, closest, n)
    elif target > tree.value:
        # make tree.value bigger
        if tree.right:
            diff_r, n_r = traverseTree(tree.right, target, closest, n)
    else:
        return [diff, tree.value]

    mi = min(diff, diff_l, diff_r)
    if mi == diff:
        return [diff, tree.value]
    elif mi == diff_l:
        return [diff_l, n_l]
    elif mi == diff_r:
        return [diff_r, n_r]


def findClosestValueInBst(tree, target):
    # Write your code here.
    closest = float('inf')
    n = float('inf')

    return traverseTree(tree, target, closest, n)[1]

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
