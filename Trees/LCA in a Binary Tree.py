"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
"""
Time: O(n)
Space: O(n)
"""
def lowestCommonAncestorInBT(root, p, q):
    if not root or root == p or root == q:
            return root
        
    # Find p/q in left subtree
    left = lowestCommonAncestorInBT(root.left, p, q)
    
    # Find p/q in right subtree
    right = lowestCommonAncestorInBT(root.right, p, q)
    
    # If p and q found in left and right subtree of this node, then this node is LCA
    if left and right:
            return root
    
    # Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
    return left if left else right