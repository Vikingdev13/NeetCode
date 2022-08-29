"""
Given a string s, find the length of the longest substring without repeating characters
"""
"""
*** My initial thought was to just add characters to a set then return the length of that set, since it cant have duplicates. But, 
this poses an issue since the problem states the length of the longest SUBSTRING. If I do this then examples like 'pwwkew' will have a set length of 4 {p,w,k,e}, 
and while the set length is correct, the proper substring would be 'wke'. 'pwke' is a SUBSEQUENCE and not a SUBSTRING.
SUBSTRING = contiguous sequence of characters of a string
SUBSEQUENCE = can be any characters of a string without changing the order in which they appear
EX: s = 'ABCD'
a substring of s could be 'AB' or 'CD'
a subsequence of s could be 'A', 'B', 'C', 'D', 'AB', 'ABC', 'ACD'...etc but NOT 'CBD' since B comes before C in the string s
"""
# Brute Force method
# Time: O(n^3) | Space: O(n)
def longestSubarrayWithoutReapeating(nums):
    result = 0
    
    for i in range(len(nums)): # O(n^2) time for nest for loop
        for j in range(i, len(nums)):
            if nums[j] in nums[i:j]: # O(n) time and space required here 
                break
            result = max(result, j - i + 1)
    return result

"""
Time: O(n)
Space: O(n)
"""
def lengthOfLongestSubstring(s):
    # Initialize an empty set, a result or counter variable to 0, and the left pointer to the beginning of the string
    hashSet = set()
    result = 0
    left = 0
    # We'll move the right pointer through the string first
    for right in range(len(s)):
        # check to see if a character is in the set, if so, we'll remove it and move the left pointer to the right
        # the right pointer has already placed the character into the set, so if the left pointer happens upon a duplicate
        # character that is already in the set, we will remove it and increment the left pointer
        while s[right] in hashSet:
            hashSet.remove(s[left])
            left += 1
        # else we will add that character to the set and then take the len of the set and compare it to the number stored in result
        # and whichever is higher, that is the new value stored in result
        hashSet.add(s[right])
        result = max(result, len(hashSet))
    return result

s = 'abcabcbb'
print(lengthOfLongestSubstring(s))