"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""
"""
Time:
Space:
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, s, t):
            # if both tree are empty
            if not s and not t:
                return True
            # if both trees are not empty and the nodes are the same, recursively keep searching
            if s and t and s.val == t.val:
                return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
            # one of the trees are empty
            return False
            
    def isSubtree(self, root, subRoot):
        # if subRoot is empty, that's still a subtree of root
        if not subRoot:
            return True
        # if root is empty, but subRoot isnt, there's no way it can be a subtree
        if not root:
            return False
        # if we've found a matching subtree
        if self.sameTree(root, subRoot):
            return True
        # recursively search the left and right subtrees
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        

root = [3,4,5,1,2]
subRoot = [4,1,2]
print(isSubtree(root,subRoot))