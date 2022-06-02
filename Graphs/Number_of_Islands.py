"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
"""
Time: O(m*n)
Space: O(m*n)
"""

def isValidCell(grid, row, col):
    try:
        return row >= 0 and col >= 0 and grid[row][col] == "1"
    except IndexError:
        return False

def dfs(grid, row, col):
    if not isValidCell(grid, row, col):
        return
    grid[row][col] = 0
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i, j in directions:
        dfs(grid, row + i, col + j)

def numIslands(grid):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                result += 1
                dfs(grid, i, j)
    return result

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))