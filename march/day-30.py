'''
This problem was asked by Google.

A unival tree (which stands for "universal value")
is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

'''


def is_unival(root):
    return unival_helper(root, root.value)


def unival_helper(root, value):
    if root is None:
        return True

    if root.value == value:
        return unival_helper(root.left, value) and \
            unival_helper(root.right, value)

    return False


def count_unival_subtrees(root):
    if root is None:
        return 0

    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)

    if is_unival(root):
        return 1 + left + right
    else:
        return left + right
