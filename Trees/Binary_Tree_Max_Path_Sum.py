"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""
"""
Time: O(n)
Space: O(h) : where h is the tree height, to keep the recursion call stack
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxPathSum(root):
    # global value set initially to the root value
    result = [root.val]

    # max path sum without splitting
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        # dealing with potential negatives
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # compute max path sum WITH splitting
        result[0] = max(result[0], root.val + leftMax + rightMax)

        # we cant choose both left and right max bc that means we're splitting
        return root.val + max(leftMax, rightMax)

    dfs(root)
    return result[0]
        



root = [1,2,3]
print(maxPathSum(root))