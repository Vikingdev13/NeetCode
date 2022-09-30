"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
"""
Time: O(n)
Space: O(n) - this can be done in O(1) space using a hashMap
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    # Preorder = (Root, Left, Right)
    # So if preorder = [3,9,20,15,7], the root is 3
    # Inorder = (Left, Root, Right)
    # And if inorder = [9,3,15,20,7], then we see 3, everything to the left of that is the left subtree and 
    # everything to the right of it is the right subtree.
    # We know that the root in preorder is the first value. 
    # Using this, we can find that root value inside the inorder array, 
    # which will give us the mid value
    root = TreeNode(preorder[0])
    mid =  inorder.index(preorder[0])

    # Now that we have the root, we can build the left and right subtrees
    root.left = buildTree(preorder[1: mid + 1], inorder[: mid + 1])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(buildTree(preorder, inorder))