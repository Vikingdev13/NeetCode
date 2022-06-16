"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
##### RECURSIVE DFS SOLUTION
"""
Time: O(n)
Space: O(n) : because of the recursive call stack
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root):
    # if the tree is empty, return 0
    if not root:
        return 0
    else:
        # recursively run down left and right subtrees and increase the depth count
        leftDepth = maxDepth(root.left)
        rightDepth = maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1
    

root = [3,9,20,None,None,15,7]
print(maxDepth(root))

##### ITERATIVE DFS SOLUTION
"""
Time: O(n)
Space: O(n)
"""
def iterativeDFS(root):
    
    stack = [[root,1]]
    result = 0

    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return result
    
