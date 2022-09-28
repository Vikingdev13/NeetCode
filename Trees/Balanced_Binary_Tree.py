"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""
Time: O(n)
Space: O(n)
"""
def isBalanced(root):

    def dfs(root):
        if not root:
            return [True, 0]
        left, right = dfs(root.left), dfs(root.right)
        # balanced is true when the left and right subtrees are balanced and the 
        # abs of the left and right heights after the root
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]
    # the inner function returns 2 values, but we only want the first value of that return statement, which is the boolean value
    return dfs(root)[0]
