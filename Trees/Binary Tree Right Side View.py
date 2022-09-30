"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
"""
Time: O(n)
Space: O(d) - where d is the tree diameter
"""
from collections import deque
def rightSideView(root):
    q = deque([root])
    result = []
    if not root:
        return []

    while q:
        levelLen = len(q)

        for i in range(levelLen):
            node = q.popleft()
            # if it's the rightmost element
            if i == levelLen - 1:
                result.append(node.val)

            # if child nodes in the queue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result

def rightSideViewRecursive(root):
    result = []
    def dfs(node, depth):
        
        if not node:
            return []

        if node:
            if depth == len(result):
                result.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
    dfs(root, 0)
    return result