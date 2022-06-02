"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
"""
Time: O(n^2)
Space: O(1)
"""
def countEvenPalindromes(s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result
        
def countPalindromes(s):
    result = 0
    for i in range(len(s)):
        result += countEvenPalindromes(s, i, i)
        result += countEvenPalindromes(s, i, i+1)
    return result

s = 'abcbda'
print(countPalindromes(s))