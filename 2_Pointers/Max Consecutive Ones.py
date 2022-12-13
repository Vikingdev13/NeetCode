"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

EX:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""
"""
Time: O(n)
Space: O(1)
"""
def maxConsecutiveOnes(nums):
    ans, count, left = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] == 1:
            count += 1
        else:
            left = right
            count = 0
        ans = max(ans, count)
    return ans

print(maxConsecutiveOnes([1,1,0,1,1,1])) # -> 3
print(maxConsecutiveOnes([1,0,1,1,0,1])) # -> 2