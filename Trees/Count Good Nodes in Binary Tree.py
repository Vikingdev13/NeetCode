"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""
"""
Time: O(n)
Space: O(h)
"""
def goodNodes(root):
    def dfs(node, maxSoFar):
        if not root:
            return 0

        result = 1 if node.val >= maxSoFar else 0            
        maxSoFar = max(maxSoFar, node.val)
        result += dfs(node.left, maxSoFar)
        result += dfs(node.right, maxSoFar)
        return result
    return dfs(root, root.val)
    
