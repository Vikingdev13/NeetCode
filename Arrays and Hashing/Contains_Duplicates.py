"""
PROBLEM STATEMENT:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct
"""


"""
Timsort = O(nlog(n))
nested for loops = O(n^2)
Time: O(n^2)
Space: O(n)
"""
def containsDuplicates1(nums):
    nums.sort()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


nums = [1,2,3,1]
print(containsDuplicates1(nums))

"""
set = O(n)
Time: O(n)
Space: O(n)
"""
def containsDuplicates2(nums):
    hashSet = set()

    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False

nums = [1,2,3,1]
print(containsDuplicates2(nums))