"""
Given an m x n matrix, return all elements of the matrix in spiral order.

The overall idea is to traverse the matrix starting from top left element and moving as far right as we can, then go down as far as we can, then left as far as we can and back up until we hit a value we've already visited. Then shift the left/right and top/bottom pointers and repeat until all values have been visited.
"""
"""
Time: O(m*n) - dimensions of the matrix
Space: O(1) - output not counted
"""
def spiralOrder(matrix):
    result = []
    left, right = 0, len(matrix[0]) # right = num of cols + 1
    top, bottom = 0, len(matrix)    # bottom = num of rows

    while left < right and top < bottom:
        # get every val in top row(left to right)
        for i in range(left, right): # right is technically out of bounds, but python loop is not inclusive, so right - 1 is still in bounds
            result.append(matrix[top][i])
        # update top by shifting down by 1
        top += 1

        # get every val in right column(top to bottom)
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        # update right by shifting to left
        right -= 1
        # if the pointers have crossed
        if not (left < right and top < bottom):
            break

        # get every val from bottom row(right to left)
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])
        # update botom by shifting up by 1
        bottom -= 1

        # get every val in left column(bottom to top)
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        # update left by shifting right by 1
        left += 1
    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]] # -> [1,2,3,6,9,8,7,4,5]
print(spiralOrder(matrix))