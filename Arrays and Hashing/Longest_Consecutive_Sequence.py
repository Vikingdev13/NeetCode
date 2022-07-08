"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
"""
Time: O(n)
Space: O(n)
"""
def longestConsecutive(nums):
    numSet = set(nums)
    count = 0
    
    for num in nums:
        if (num-1) not in numSet:
            length = 0
            while (num + length) in numSet:
                length += 1
            count = max(count, length)
    return count
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))