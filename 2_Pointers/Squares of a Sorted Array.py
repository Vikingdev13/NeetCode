"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

EX:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""
"""
Time: O(nlogn)
Space: O(n)
"""
# Brute Force Solution
def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return sorted(result)

# Optimized Solution
"""
Time: O(n)
Space: O(n) - unless you don't count the output, then O(1)
"""
def sortedSquaresOptimized(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1

    for i in range(n-1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result

    