"""
Given an array containing 0s and 1s, if you are allowed to replace no more than k 0s with 1s, find the length of the longest contiguous subarray having all 1s
"""
"""
Time: O(n)
Space: O(1)
"""
def length_of_longest_substring(nums, k):
    left = numOfOnes = maxLen = 0

    for right in range(len(nums)):
        # if the val of right ptr is a 1, update the ones counter
        if nums[right] == 1:
            numOfOnes += 1
        # if the window size - the count of 1 and the remaining 0s are greater than k
        if (right-left+1 - numOfOnes) > k:
            # if the val of the left ptr is a 1, update the ones counter
            if nums[left] == 1:
                numOfOnes += 1
            left += 1
        maxLen = max(maxLen, (right-left+1))
    return maxLen

nums = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2
print(length_of_longest_substring(nums, k))