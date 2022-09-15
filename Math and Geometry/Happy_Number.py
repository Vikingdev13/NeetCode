"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""
"""
Time: O(logn)
Space: O(logn)
"""
def isHappy(num):
    
    def getNextNum(n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total

    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = getNextNum(num)
    return num == 1
  
print(isHappy(19))    # -> True
print(isHappy(2))     # -> False
print(isHappy(13456)) # -> False