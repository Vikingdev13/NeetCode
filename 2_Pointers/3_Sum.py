"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets
"""
"""
Time: O(n^2)
Space: O(1) to O(n) - depends on sorting algorithm, in this instance I used TimSort which is O(n) space
"""
def threeSum(nums):
    result = []
    # sort input array first
    nums.sort()

    for indx, val in enumerate(nums):
        # don't want to reuse the same val at the same position twice, so continue traversing array
        if indx > 0 and val == nums[indx-1]:
            continue
        # 2 pointer approach for the rest of the array
        left, right = indx + 1, len(nums) - 1
        while left < right:
            # compute sum
            threeSum = val + nums[left] + nums[right]
            # if sum is too high, move right ptr
            if threeSum > 0:
                right -= 1
            # else if the sum is too small, move left ptr
            elif threeSum < 0:
                left += 1
            # else the sum is what we're looking for, so append those vals to the output array
            else:
                result.append([val, nums[left], nums[right]])
                left += 1
                # making sure that we dont use the same vals again
                # EX: [-2,-2,0,0,2,2]
                # -2 + 2 = 0, so the left ptr will move right and its val is the same as the val before it,
                # so it needs to move right again until it finds a val that isnt the same as the prev one, 
                # while the conditions of the if statement above will handle the right ptr.
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result
                    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))