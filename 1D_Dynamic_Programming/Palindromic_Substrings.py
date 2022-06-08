"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
"""
Time: O(n^2)
Space: O(1)
"""
def countPalindromesWithCenter(s, left, right):
        result = 0
        # while staying within the boundaries of the input strings len 
        # and that the character at s[left] == s[right]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # update result and move the left/right indices
            result += 1
            left -= 1
            right += 1
        return result
        
def countPalindromes(s):
    result = 0
    for i in range(len(s)):
        # count odd len palindromes
        result += countPalindromesWithCenter(s, i, i)
        # count even len palindromes
        result += countPalindromesWithCenter(s, i, i+1)
    return result

s = 'google'
print(countPalindromes(s))