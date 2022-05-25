"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from numpy import product

"""
*** Naive Approach ***
Time: O(n)
Space: O(1) - problem states that output array does not count in memory calculation, otherwise it would be O(n)
But problem statement does not want us to use division operation so we must find another way.
"""
def productExceptSelf(nums):
    result = []
    prodOfInput = product(nums)
    
    for num in nums:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        else:
            result.append(prodOfInput//num)
    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))

"""
Optimal Approach
Time: O(n)
Space: O(1) - the output array doesn't count as memory for the context of this problem
"""
def productExceptSelf2(nums):
    # fill result array with all 1s ** could be all 0s too, either one is fine
    result = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    # result = [1,1,2,6] up to this point
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i]
    return result
nums = [1,2,3,4]
print(productExceptSelf2(nums))