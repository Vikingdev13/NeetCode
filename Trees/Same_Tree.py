"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
"""
Time: O(n)
Space: O(n)
"""
def sameTree(p, q):
    # if p and q are empty
    if not p and not q:
        return True
    # if one of the tree's p or q are empty or a node in the same position in both p and q arent equal
    if not p or not q or p.val != q.val:
        return False
    # recursively iterate through both trees subtrees
    return (sameTree(p.left, q.left) and sameTree(p.right, q.right))

p = [1,2,3]
q = [1,2,3]
print(sameTree(p,q))