"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
def containerWithMostWater(height):
    # Initialize a result variable and 2 pointers, left and right, where left is at the beginning or array and right is at the end
    result = 0
    left, right = 0, len(height) - 1
    # while the left and right pointers haven't touched, compute the maxArea between those two pointers and store the greater value
    # between what is stored in result and maxArea in result
    while left < right:
        # to compute the maxArea, take the difference of the right pointer index and left pointer index and multiply it by the 
        # minimum value between where the left and right pointers sit
        # EX: On the first iteration of the given array height, it would look like this:
        # maxArea = (8-0) * min(1,7) = 8 * 1 = 8
        # result = max(0,8) which result will equal 8 now
        maxArea = (right - left) * min(height[left], height[right])
        result = max(result, maxArea)
        # After computing the area between the vertical lines(walls), we need to move the pointers
        # if the value of the left pointer is  less than the value of the right pointer, move the left pointer to the right 1 space
        if height[left] < height[right]:
            left += 1
        # else the value of the right pointer is less than the value of the right pointer, move the right pointer to the left 1 space
        # then move back up to the while loop conditions
        else:
            right -= 1
    return result

height = [1,8,6,2,5,4,8,3,7]
print(containerWithMostWater(height))