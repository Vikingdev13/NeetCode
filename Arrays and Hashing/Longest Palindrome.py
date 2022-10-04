
"""
Time: O(n)
Space: O(n)
"""
def longestPalindrome(s):
    from collections import Counter

    freq = Counter(s)
    odd = False
    result = 0

    for val in freq.values():
        # if the char count is even
        if val % 2 == 0:
            result += val
        # else the char count is odd
        else:
            result += val - 1
            odd = True
    if odd:
        result += 1
    return result

print(longestPalindrome('abccccdd'))