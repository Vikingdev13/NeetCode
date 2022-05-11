"""
PROBLEM STATEMENT:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
*** Brute Force approach ***
nested for loops = O(n^2)
Time: O(n^2)
Space: O(1)
"""
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

nums = [2,7,4,10,6,8,-1,5]
target = 14
print(twoSum(nums, target))

"""
*** Optimized approach ***
Time: O(n) **O(1) avg case since hashMaps have constant lookup avg case
Space: O(n)
"""
def twoSumOptimized(nums, target):
    hashMap = {}

    for indx, val in enumerate(nums):
        difference = target - val
        if difference in hashMap:
            return [hashMap[difference], indx]
        hashMap[val] = indx

print(twoSumOptimized(nums, target))