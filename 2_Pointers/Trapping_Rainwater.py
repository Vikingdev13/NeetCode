"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
"""
Time: O(n): since we have to traverse the entire array
Space: O(1): only using constant space for variables, no extra DS used
"""
def trap(height):
    if not height:
        return 0

    left, right = 0, len(height)-1
    leftMax, rightMax = height[left], height[right]
    totalWater = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            totalWater += leftMax - height[left]

        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            totalWater += rightMax - height[right]
    return totalWater

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))