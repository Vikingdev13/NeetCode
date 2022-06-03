"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""
"""
Time: O(m*n)
Space: O(m*n)
"""
def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(row, col, visited, prevHeight):
        # check that position has not been visited yet, or out of bounds of grid, or that the current height is lower than the prev height 
        if ((row,col) in visited or row < 0 or col < 0 or row == rows or col == cols or heights[row][col] < prevHeight):
            return
        # add position to visited and recursively visit all positions near it
        visited.add((row, col))
        dfs(row + 1, col, visited, heights[row][col])
        dfs(row - 1, col, visited, heights[row][col])
        dfs(row, col + 1, visited, heights[row][col])
        dfs(row, col - 1, visited, heights[row][col])

    # iterate through the rows
    for col in range(cols):
        dfs(0, col, pacific, heights[0][col])
        dfs(rows - 1, col, atlantic, heights[rows-1][col])

    # iterate through the cols
    for row in range(rows):
        dfs(row, 0, pacific, heights[row][0])
        dfs(row, cols - 1, atlantic, heights[row][cols-1])

    # iterate through all positions in grid
    result = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])
    return result

heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]
           ]
print(pacificAtlantic(heights))