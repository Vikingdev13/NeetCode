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
            # return the [index of value where the key=diff, and the current indx]
            # EX: for the array nums above, hashMap contains for following key/val pairs at the 4th iteration of loop
            # 2 : 0
            # 7 : 1
            # 4 : 2
            # diff will equate to 4 bc 14 - 10 = 4, and 4 IS in the hashMap, so return the val of that key/val pair and the current index we're at
            # returns [2,3]
            return [hashMap[difference], indx]
        hashMap[val] = indx

print(twoSumOptimized(nums, target))