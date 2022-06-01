"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations
"""
"""
Time: O(n)
Space: O(n)
"""
def characterReplacement(s, k):
    count = {}
    result = left = maxFreq = 0
    
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right],0)
        maxFreq = max(maxFreq, count[s[right]])

        while (right - left + 1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result

s = 'AABABBA'
k = 1
print(characterReplacement(s, k))