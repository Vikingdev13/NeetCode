"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**** Will need to clarify the above if not initially told so. Ask if only horizontally or vertically count or if diagonally too. The difference really only comes to the directions you specify the algo to move
"""
"""
Time: O(m*n)
Space: O(m*n)
"""

def isValidCell(grid, row, col):
    try:
        # make sure we're not out of bounds and look for cells marked with a 1, which is a land cell
        return row >= 0 and col >= 0 and grid[row][col] == "1"
    except IndexError:
        return False

def dfs(grid, row, col):
    # if not a validCell, meaning a cell marked a 1, move to another cell
    if not isValidCell(grid, row, col):
        return
    # else mark the valid cell with a 0 so we know we've visited it already
    grid[row][col] = 0
    # store a list of pairs that represent the directions from a cell
    # directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1,-1], [-1,1], [1,1], [1,-1]] # use this if diagonally cells can count
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # iterate over the directions to move to nearby cells
    for i, j in directions:
        dfs(grid, row + i, col + j)

def numOfIslands(grid):
    # initialize a counter variable to store how many islands we find
    numIslands = 0
    # iterate over every row
    for i in range(len(grid)):
        # iterate over every column
        for j in range(len(grid[0])):
            # if the cell is a land cell, update numIslands counter
            if grid[i][j] == "1":
                numIslands += 1
                # call the dfs function to visit and mark the neighboring cells 
                # of the cell we just found that is a land cell
                dfs(grid, i, j)
    return numIslands



grid = [
  ["1","1","0","0","1"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# grid = [[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
# 	    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
# 	    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
# 	    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
# 	    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
# 	    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
# 	    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
# 	    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
# 	    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
# 	    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
#        ]

print(numOfIslands(grid))