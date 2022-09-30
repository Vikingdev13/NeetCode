"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
"""
Time: O(n)
Space: O(h)
"""
from collections import deque
def levelOrder(root):
    # BFS
    result = []
    q = deque()
    if root:
        q.append(root)

    while q:
        val = []

        for _ in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(val)
    return result