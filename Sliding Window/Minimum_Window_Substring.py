"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string
"""
"""
Time: O(n+m)
Space: O(n)
"""
def get_minimum_window(original, check):
    left, matched, substr_start = 0, 0, 0
    min_length = len(original) + 1
    charFreq = {}

    for chr in check:
        if chr not in charFreq:
            charFreq[chr] = 1 + charFreq.get(chr, 0)
        

    # try to extend the range [left, right]
    for right in range(len(original)):
        right_char = original[right]
        if right_char in charFreq:
            charFreq[right_char] -= 1
            if charFreq[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(check):
            if min_length > right - left + 1:
                min_length = right - left + 1
                substr_start = left

            left_char = original[left]
            left += 1
            if left_char in charFreq:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if charFreq[left_char] == 0:
                    matched -= 1
                charFreq[left_char] += 1

    if min_length > len(original):
        return ""
    return original[substr_start:substr_start + min_length]

original = "ADOBECODEBANC"
check = "ABC"
print(get_minimum_window(original, check))