"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time
"""
# We have some clues on how to go about solving this. We're given a SORTED array already, 
# and we need to write an algorithm in O(log(n)) time. To me, this tells me Binary Search.
"""
Time: O(log(n))
Space: O(1)
"""

def minInRotatedSortedArray(nums):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        # if the val at nums[mid] is less than or equal to the last number in the array,
        # then update the index to equal nums[mid] and move the right ptr to the left
        # because that means the values to the right of mid are all too high
        if nums[mid] <= nums[-1]:
            index = nums[mid]
            right = mid - 1
        else:
            left = mid + 1
    return index


nums = [3,4,5,1,2]
print(minInRotatedSortedArray(nums))