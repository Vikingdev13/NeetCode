"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
"""
Time: O(n)
Space: O(1)
"""
def jumpGame2(nums):
    count = 0
    left, right = 0, 0

    while right < len(nums)-1:
        farthest = 0
        for i in range(left, right+1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        count += 1
    return count


print(jumpGame2([2,3,1,1,4])) # -> 2