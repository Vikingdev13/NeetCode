"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity
"""

"""
Time: O(log(n))
Space: O(1)
"""

def binarySearch(nums, target):
    # initialize a pointer at the beginning and the end of the array
    left, right = 0, len(nums) - 1
    # while the pointers haven't met yet....
    while left <= right:
        # initialize a variable called mid, which will be set at the middle of the array
        mid = (left + right) // 2
        # if the value at mid is our target, you've found it, you're done return the index
        if nums[mid] == target:
            return mid
        # if the val at mid is greater than our target value, then we know that everything 
        # after mid cannot be our target since it is sorted in ascending order, so we move
        # the right pointer to the left and skip over all the values to the right of mid
        if nums[mid] > target:
            right = mid - 1
        # else the val at mid is less than our target value, and we know that everything 
        # before mid cannot be our target value since it's sorted, so we can move the left pointer
        # right to the val of mid + 1
        else:
            left = mid + 1
    return -1

nums = [-1,0,3,5,9,12]
target = 5
print(binarySearch(nums,target))