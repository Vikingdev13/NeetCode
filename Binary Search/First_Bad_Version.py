"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
"""
Time: O(log(n))
Space: O(1)
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def firstBadVersion(n):
    # Binary Search Solution
    # first we initialize our pointers
    # since the constraints are 1 <= bad <= n <= n^31-1, n will never be below 1 
    # and then the right pointer will be set to whatever value n is
    left, right = 1, n

    # iterate the 2 pointers
    while left < right:
        mid = (left+right)//2
        # call to API, if the val of mid is True then we set the right ptr to the val of mid, 
        # this means that all of the values after mid are bad versions so we dont need to look 
        # that direction anymore, and that the FIRST bad version is to the left of mid
        # Keep reducing until we find the first value or true that comes after the last false 
        # and return that value of left
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left