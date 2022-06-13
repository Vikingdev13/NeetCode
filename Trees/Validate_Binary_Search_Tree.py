"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""
"""
Time:
Space:
"""
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):

    # helper function
    def valid(node, left, right):
        # even an empty BST is still a valid BST
        if not node:
            return True
        # boundary checks
        # -inf < node.val < inf
        if not(node.val < right and node.val > left):
            return False
        # check the boundaries of left and right subtrees
        return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
    return valid(root, float('-inf'), float('inf'))