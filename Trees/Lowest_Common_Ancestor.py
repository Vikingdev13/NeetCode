"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
"""
Time: O(log(n)) - I believe this is log(n) since it checks the val of the nodes p & q, and cuts the tree in half based on that, which is a binary search
Space: O(1)
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    curr = root
    # while curr is not null
    while curr:
        # check the values of p and q, if they're both greater than the current node val, 
        # traverse down the right subtree
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        # check the values of p and q, if they're both less than the current node val, 
        # traverse down the left subtree
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr