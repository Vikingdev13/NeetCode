"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
"""
Time: O(n^2)
Space: O(1)
"""
def countEvenPalindromes(input, left, right):
        result = 0
        while left >= 0 and right < len(input) and input[left] == input[right]:
            result += 1
            left -= 1
            right += 1
        return result
        
def countPalindromes(input):
    result = 0
    for i in range(len(input)):
        result += countEvenPalindromes(input, i, i)
        result += countEvenPalindromes(input, i, i+1)
    return result

s = 'abcbda'
print(countPalindromes(s))