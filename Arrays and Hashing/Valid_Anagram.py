"""
PROBLEM STATEMENT:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""
*** Brute Force approach ***
Time: O(nlog(n))
Space: O(n)
"""
s = 'anagram'
t = 'nagaram'

def validAnagram(s,t):
    return sorted(s) == sorted(t)

print(validAnagram(s,t))


"""
*** Optimized approach ***
Time: O(n)
Space: O(n)
"""
def validAnagramOptimized(s, t):
    # edge case: if length of t !=  length of s, it cant be an anagram
    if len(s) != len(t):
        return False
    # initialize 2 empty hashMaps
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        # put all chars of s and t into their respective hashMaps
        # and keep a count of how many of each char
        s_map[s[i]] = 1 + s_map.get(s[i], 0)
        t_map[t[i]] = 1 + t_map.get(t[i], 0)

    # iterate through s hashMap and check to see if the char and count = that of t hashMap
    for ch in s_map:
        if s_map[ch] != t_map.get(ch,0):
            return False
    return True

print(validAnagramOptimized(s,t))
