"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
"""
Time: O(n^2)
Space: O(1)
"""
def rotate(matrix):
    # set boundaries
    left, right = 0, len(matrix)-1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save top left val
            topLeft = matrix[top][left + i]
            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left into top right
            matrix[top + i][right] = topLeft
        # update pointers
        left += 1
        right -= 1
    return matrix # it says don't return anything but I did to test output, you dont need this line on LC site

matrix = [[1,2,3], # [[7,4,1],
          [4,5,6], #  [8,5,2],
          [7,8,9]  #  [9,6,3]
          ]        #  ]

print(rotate(matrix))
