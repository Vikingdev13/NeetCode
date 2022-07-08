"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
"""
Time: O(n)
Space: O(n)

My initial thought was to sort the input, but since we have to write an algorithm that runs in O(n) time, 
that's not a good idea since sorting the input would give me a O(nlog(n))) time complexity. It's not a 
bad place to start, but will definitely need to be optimized.
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