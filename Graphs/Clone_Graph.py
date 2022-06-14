"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
"""
Time: 
Space: 
"""
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    # initialize a hashMap mapping the original nodes to the new nodes
    originalToNew = {}
    # helper function to clone the nodes
    def makeClone(node):
        # if the node has already been cloned, just return it
        if node in originalToNew:
            return originalToNew[node]
        # clone the next node that hasn't been cloned already
        copy = Node(node.val)
        # then map its old node to the new copy
        originalToNew[node] = copy
        # recursively move down a nodes neighbors and clone the ones not already cloned
        for neighbor in node.neighbors:
            copy.neighbors.append(makeClone(neighbor))
        return copy
    # return the new graph unless it was an empty graph then return null
    return makeClone(node) if node else None

adjList = [[2,4],[1,3],[2,4],[1,3]]
print(cloneGraph(adjList))