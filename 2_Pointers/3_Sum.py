"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets
"""
"""
Time: O(n^2)
Space: O(n) or O(1) - depends on the languages sorting library and implementation
"""
def threeSum(nums):
    result = []
    nums.sort()

    for indx, val in enumerate(nums):
        if indx > 0 and val == nums[indx-1]:
            continue

        left, right = indx + 1, len(nums) - 1
        while left < right:
            threeSum = val + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                result.append([val, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result
                    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))