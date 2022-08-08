"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
"""
Time: O(n)
Space: O(n)
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    result = [0]

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        result[0] = max(result[0], 2 + left + right)

        return 1 + max(left, right)
    dfs(root)
    return result[0]
    
    

if __name__ == "__main__":
    root = [1,2,3,4,5]

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c
    b.left = d
    b.right = e


    print(diameterOfBinaryTree(a)) # -> 3