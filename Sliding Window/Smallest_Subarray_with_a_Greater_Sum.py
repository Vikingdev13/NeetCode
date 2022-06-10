"""
Given an array of positive integers and a number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S. Return 0 if no such subarray exists
"""
"""
Time:
Space:
"""
def smallest_subarray_sum(arr, S):
    left = windowSum = 0
    minLen = float('inf')

    for right in range(len(arr)):
        windowSum += arr[right]

        while windowSum >= S:
            minLen = min(minLen, (right-left+1))
            windowSum -= arr[left]
            left += 1
    if minLen == float('inf'):
        return 0
    return minLen


arr = [2, 1, 5, 2, 3, 2]
S = 7
print(smallest_subarray_sum(arr, S))