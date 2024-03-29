"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""
"""
Time: O(n)
Space: O(n)
"""
# class TreeNode:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = None
#         self.right = None

def isValidBST(root):

    # helper function that sets the boundaries of low and high
    def validate(node, low = float('-inf'), high = float('inf')):
        # an empty BST is still a valid BST
        if not node:
            return True
        # the current node's val must be between low and high
        if node.val <= low or node.val >= high:
            return False
        # the left and right subtree must also be valid
        # we will compare the node vals of the left subtree to ensure that the curr node val is greater than the low or -inf and 
        # less than the curr node's parent val.
        # Likewise, the right subtree will be tested in the same manner, except we check that the curr node's val is less than 
        # high or inf and greater than the parent of curr node
        return (validate(node.right, node.val, high) and validate(node.left, low, node.val))
    return validate(root)