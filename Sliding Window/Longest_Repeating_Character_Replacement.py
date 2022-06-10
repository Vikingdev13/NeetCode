"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations
"""
"""
Time: O(n)
Space: O(1)
"""
def characterReplacement(s, k):
    count = {}
    result = left = maxFreq = 0
    # Iterate the right ptr until the end of string s 
    for right in range(len(s)):
        # update the count of each character at position right
        count[s[right]] = 1 + count.get(s[right],0)
        # update the max frequency with the greater val of itself or the count of that curr character at pos right
        maxFreq = max(maxFreq, count[s[right]])

        # windowSize = (right - left + 1)
        # while the windowSize - max frequency is greater than k
        while ((right - left + 1)) - maxFreq > k:
            # decrement the character count of character at pos left
            count[s[left]] -= 1
            # then move the left ptr to the right(slide the window)
            left += 1
        # update result with the greater val between itself and the size of characters in window
        result = max(result, (right - left + 1))
    return result

s = 'aabccbb'
k = 2
print(characterReplacement(s, k))