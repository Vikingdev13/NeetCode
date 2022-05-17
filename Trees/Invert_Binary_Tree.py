"""
Given the root of a binary tree, invert the tree, and return its root
"""

"""
Time: O(n)
Space: O(n)
"""
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None

def invertTree(root):
    # if the tree is empty return none
    if not root:
        return None
    # here we will swap the children/subtrees
    # assign the left child to a temp variable
    # set the left child to equla the right child
    # then set the right child to the temp variable
    tmp = root.left
    root.left = root.right
    root.right = tmp

    # recursively call the function on the left and right children
    self.invertTree(root.left)
    self.invertTree(root.right)

    # lastly return root
    return root