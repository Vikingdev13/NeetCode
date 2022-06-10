"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string
"""
"""
Time: O(n+m)
Space: O(n)
"""
from collections import Counter

def get_minimum_window(original, check):
    # Counts the number of each character of "check"
    check_count = Counter(check)
    # Counts the number of each character in the sliding window
    window_count = {}
    # Count the number of entries in "check_count" that is smaller than or equal to
    # that in "window_count"
    # If "satisfy_count" is equal to the number of entries in "check_count",
    # that window contains "check". We then just need to check if its the minimum.
    satisfy_count = 0
    original_len = len(original)
    # Two pointers pointing to the window (inclusive start, exclusive end)
    start_ptr = 0
    end_ptr = 0
    # The number of entries in "check_count". Used to check if "window_count" contains
    # "check_count"
    match_req = len(check_count.keys())
    # The smallest recorded string that satisfies the conditions.
    smallest_str = None
    # Change the number of "char" inside the window by "delta"
    # Automatically increase or decrease "satisfy_count" to reflect the current value.
    def delta_char(char, delta):
        nonlocal satisfy_count
        if char not in window_count:
            window_count[char] = 0
        if window_count[char] >= check_count.get(char, 0):
            satisfy_count -= 1
        window_count[char] += delta
        if window_count[char] >= check_count.get(char, 0):
            satisfy_count += 1
    while end_ptr < original_len:
        # Moves the end pointer until it contains "check" or it reaches the end
        while end_ptr < original_len and satisfy_count < match_req:
            delta_char(original[end_ptr], 1)
            end_ptr += 1
        # If the window reaches the end and does not contain "check", break loop
        if end_ptr == original_len and satisfy_count < match_req:
            break
        # Otherwise, the window contains "check", so we move the start pointer
        # until it no longer does. Then, the one before failing the check is the local
        # minimal substring.
        while satisfy_count >= match_req:
            delta_char(original[start_ptr], -1)
            start_ptr += 1
        valid_window = original[start_ptr - 1 : end_ptr]
        # Compare the local minimum to the stored smallest string
        # If there is nothing stored, or the condition outlined is true, we store the string
        if smallest_str is None or (len(smallest_str) > len(valid_window)):
            smallest_str = valid_window
        elif len(smallest_str) == len(valid_window) and valid_window < smallest_str:
            smallest_str = valid_window
    return smallest_str or ""


original = "ADOBECODEBANC"
check = "ABC"
print(get_minimum_window(original, check))