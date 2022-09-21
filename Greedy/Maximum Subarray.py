"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
"""
Time: O(n)
Space: O(1)
"""
def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0
        currSum += num
        maxSum = max(maxSum, currSum)
    return maxSum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # -> 6
print(maxSubArray([5,4,-1,7,8]))            # -> 23
print(maxSubArray([1]))                     # -> 1
