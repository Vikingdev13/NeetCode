"""
Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.
"""
"""
Time: O(n)
Space: O(1)
"""

def subarraySum(nums, target):
    prefixSums = {0:0}
    currSum = 0

    for i in range(len(nums)):
        currSum += nums[i]
        diff = currSum - target
        if diff in prefixSums:
            return [prefixSums[diff], i + 1]
        prefixSums[currSum] = i + 1

nums = [1, -20, -3, 30, 5, 4]
target = 7
print(subarraySum(nums, target))