"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array
"""
"""
Time: O(n)
Space: O(1)
"""
def maxSubarray(nums):
    # initialize the maxSum variabe to the first element of the array since there could be negative numbers in it
    maxSum = nums[0]
    # initialize a current sum to 0
    currSum = 0
    # iterate through the array and if the current sum is negative, reset it to 0
    for num in nums:
        if currSum < 0:
            currSum = 0
        # else add the val to current sum and then update maxSum with whichever value is greater between current sum and maxSum
        currSum += num
        maxSum = max(maxSum, currSum)

    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarray(nums))