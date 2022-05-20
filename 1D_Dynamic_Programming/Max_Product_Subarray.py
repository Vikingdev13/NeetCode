"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array
"""
"""
Time: O(n)
Space: O(1)
"""
def maxProdSubarray(nums):
    result = max(nums)
    currMin, currMax = 1,1

    for num in nums:
        temp = currMax * num
        currMax = max(num * currMax, num * currMin, num)
        currMin = min(temp, num * currMin, num)
        result = max(result, currMax, currMin)
    return result

nums = [2,3,-2,4]
print(maxProdSubarray(nums))
            