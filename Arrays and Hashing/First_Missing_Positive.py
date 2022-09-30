"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""
"""
Time: O(n)
Space: O(n)
"""
def firstMissingPositive(nums):
    n = len(nums)
    hashSet = set(nums)

    for i in range(1, n+2):
        if i not in hashSet:
            return i

nums = [1,2,6,4,3,1]
print(firstMissingPositive(nums))