"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise
"""

"""
*** Naive Approach ***
Time: O(n)
Space: O(n)
"""
def validPalindrome(s):
    # initialize an empty string
    newStr = ''
    # iterate through the argument string
    for ch in s:
        # if a character in s is alphanumeric(A-Z,a-z,0-9)
        if ch.isalpha():
            # append it to the new string and lower case it
            newStr += ch.lower()
    # compare the new string to itself reversed, if the same return True, else False: Not a palindrome
    return newStr == newStr[::-1]

s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))

"""
*** 2 Pointer Approach ***
Time: O(n)
Space: O(1)
"""

def validPalindrome2(s):
    # initialize a pointer at the front and end of the string
    left, right = 0, len(s)-1
    # iterate through the string while the pointers dont touch
    while left < right:
        # while the pointers dont touch AND the val at left pointer is NOT an alphanumeric(A-Z,a-z,0-9) char, 
        # so like a space or puncuation, increment the left pointer to the right 1 place at a time
        while left < right and not s[left].isalnum():
            left += 1
        # while the pointers dont touch AND the val at right pointer is NOT an alphanumeric(A-Z,a-z,0-9) char, 
        # so like a space or puncuation, increment the right pointer to the left 1 place at a time
        while left < right and not s[right].isalnum():
            right -= 1
        # if the pointers haven't met yet AND the values at the left pointer and right pointer aren't equal, return False
        if left < right and s[left].lower() != s[right].lower():
            return False
        # Else they're equal and we can move the left and right pointer to the next char in the string
        left += 1
        right -= 1
    return True
    

print(validPalindrome2(s))

"""
2 Pointer approach using your own built alpha numeric method
Time: O(n)
Space: O(1)
"""
def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def validPalindrome3(s):
    left, right = 0, len(s) -1

    while left < right:
        while left < right and not alphanum(s[left]):
            left += 1
        while left < right and not alphanum(s[right]):
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(validPalindrome3(s))