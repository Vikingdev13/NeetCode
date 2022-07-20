"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
"""
"""
Time:
Space:
"""
def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1

    # Using binary search, we will determine which row to begin our search for the target. We can accomplish 
    # this using the properties above, knowing that the rows are sorted and that the first number in each row 
    # is larger than the last number of the prev row.
    while top <= bottom:
        # this is our current row to run binary search on
        row = (top+bottom)//2
        # if the target is greater than the last integer of the row(which is the largets in the row), move down to the next row
        if target > matrix[row][-1]:
            top = row + 1
        # else if the target is less than the first integer of the row(which is the smallest in the row), move up to the next row
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    # if none of the rows contains the target value, return False
    if not (top <= bottom):
        return False
    row = (top+bottom)//2
    left, right = 0, COLS - 1

    while left <= right:
        mid = (left+right)//2
        # if the target value is greater than the value at mid in this row
        if target > matrix[row][mid]:
            left = mid + 1
        # else if the target the less than the value at mid in this row
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    return False

    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))