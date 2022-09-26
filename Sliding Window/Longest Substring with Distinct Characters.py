"""
Given a string, find the length of the longest substring, which has all distinct characters.
"""
"""
Time: O(n)
Space: O(K)
"""
def longestSubstringDistinctChars(s):
    left, maxLen = 0, 0
    freq = {}

    for right in range(len(s)):
        charRight = s[right]

        if charRight in freq:
            left = max(right, freq[charRight] + 1)
        freq[charRight] = right
        maxLen = max(maxLen, right - left + 1)
    return maxLen

print(longestSubstringDistinctChars("abccde")) # -> 3 'abc' or 'cde'