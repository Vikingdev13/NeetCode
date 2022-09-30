"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
"""
Time: O(n)
Space: O(n)
"""
def kSmallestInBST(root, k):
    result = []
    curr = root

    while result or curr:
        while curr:
            result.append(curr)
            curr = curr.left
        curr = result.pop()
        k -=1
        if k == 0:
            return curr.val
        curr = curr.right

