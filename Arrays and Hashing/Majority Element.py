"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
nums = [2,2,1,1,1,2,2]
"""
Brute force sorting
Time: O(nlogn)
Space: O(n)
"""
def majElementSorting(nums):
    nums.sort()
    return nums[len(nums)//2]

"""
Hastable approach
Time: O(n)
Space: O(n)
"""
def majElementHash(nums):
    from collections import Counter
    count = Counter(nums)
    return max(count.keys(), key=count.get)
"""
Time: O(n)
Space: O(1)
"""
def majorityElement(nums):
    count = 0
    majElement = None

    for num in nums:
        if count == 0:
            majElement = num
        count += (1 if num == majElement else -1)
    return majElement

print(majElementSorting(nums))  # -> 2
print(majElementHash(nums))     # -> 2
print(majorityElement(nums))    # -> 2