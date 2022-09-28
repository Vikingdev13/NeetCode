"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill
sr = source row
sc = source column
"""
"""
Time: O(n)
Space: O(n)
"""
def floodFill(image, sr, sc, newColor):
    # if the image is none or the image is already the new color, we dont need to do anything
    if image == None or image[sr][sc] == newColor:
        return image
    # else call the function fill recursively
    fill(image, sr, sc, image[sr][sc], newColor)
    return image
# DFS
def fill(image, row, col, initial, newColor):
    # base case: out of bounds checking
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != initial:
        return
    # change the new pixel to the new color
    image[row][col] = newColor
    fill(image, row+1, col, initial, newColor) # down
    fill(image, row-1, col, initial, newColor) # up
    fill(image, row, col+1, initial, newColor) # right
    fill(image, row, col-1, initial, newColor) # left