"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
"""
Time: O(n)
Space: O(1)
"""
def canJump(nums):
    goalPost = len(nums)-1
    # work backwards
    for i in range(len(nums)-1,-1,-1):
        # if the current indx val is able to reach the current goal post
        # move the goal post to the current indx
        if i + nums[i] >= goalPost:
            goalPost = i
    # if goal post is at 0 indx, then return True since yes there is a way to get to the last indx from the starting index, else False
    return goalPost == 0

print(canJump([2,3,1,1,4])) # -> True
print(canJump([3,2,1,0,4])) # -> False