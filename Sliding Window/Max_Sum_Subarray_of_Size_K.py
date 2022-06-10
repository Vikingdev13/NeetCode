"""
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of size k.
"""
"""
Time: O(n)
Space: O(1)
"""
def max_sub_array_of_size_k(arr, k):
    maxSum = left = windowSum = 0
    # move the right ptr through array, and add its val to windowSum
    for right in range(len(arr)):
        windowSum += arr[right]
        # if the window size is too big
        if (right-left+1) >= k:
            # update the maxSum
            maxSum = max(maxSum, windowSum)
            # subtract the val of the left ptr and increment the left ptr
            windowSum -= arr[left]
            left += 1
    return maxSum

arr = [2,1,5,1,3,2]
k = 3
print(max_sub_array_of_size_k(arr, k))