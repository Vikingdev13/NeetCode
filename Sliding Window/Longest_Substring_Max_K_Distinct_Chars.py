"""
Given a string, find the length of the longest substring in it with no more than K distinct characters
"""
"""
Time: O(n)
Space: O(k) - depending on the val of k, we could end up putting the whole string into the hashMap
"""
def longest_substring_with_k_distinct(str1, k):
    charFreq = {}
    start = maxLen = 0
    # iterate through the atring char by char
    for end in range(len(str1)):
        charRight = str1[end]
        # if the current char is not in the hashMap, add it and update its frequency count
        if charRight not in charFreq:
            charFreq[charRight] = 1 + charFreq.get(charRight, 0)

        # while the length of the hashMap is greater than the val k, 
        # keep shrinking the window size until we're left with k distinct chars 
        while len(charFreq) > k:
            charLeft = str1[start]
            # remove the char the left ptr points to
            charFreq[charLeft] -= 1
            if charFreq[charLeft] == 0:
                del charFreq[charLeft]
            start += 1
        maxLen = max(maxLen, end-start+1)
    return maxLen


str1 = "araaci"
k = 2
print(longest_substring_with_k_distinct(str1, k))