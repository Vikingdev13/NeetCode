"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string
"""
"""
Time: O(n)
Space: O(n)
"""
from collections import Counter


def minWindow(s, t):
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = 1 + window_counts.get(character, 0) 

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))