"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
"""
Time: O(nlogn)
Space: O(n)

Brute force approach and ignoring the last statement in the instructions about using built in sorting
"""
def sortColors(nums):        
    return sorted(nums)

print(sortColors([2,0,1]))          # -> [0,1,2]
print(sortColors([2,0,2,1,1,0]))    # -> [0,0,1,1,2,2]

"""
Time: O(n)
Space: O(1)

2 Pointer approach, sorts in place
"""
def optimizedSortColors(nums):
    left, right = 0, len(nums)-1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            i += 1
            left += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
    return nums

print(optimizedSortColors([2,0,1]))         # -> [0,1,2]
print(optimizedSortColors([2,0,2,1,1,0]))   # -> [0,0,1,1,2,2] 