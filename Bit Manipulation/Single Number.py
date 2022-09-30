"""
In a non-empty array of integers, every number appears twice except for one, find that single number.
"""

"""
Time: O(n)
Space: O(1)
"""
def singleNum(nums):
    num = 0
    for i in nums:
        num ^= i
    return num

print(singleNum([1, 4, 2, 1, 3, 2, 3])) # -> 4