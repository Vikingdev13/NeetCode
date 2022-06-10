"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.
"""
"""
Time: O(n + m) - where n and m are the num of chars in string and pattern
Space: O(m) - where worst case we would have to add all chars from pattern and pattern having all distinct chars
"""
def permutationsOfString(string, pattern):
    left, matched = 0, 0
    charFreq = {}

    for ch in pattern:
        if ch not in charFreq:
            charFreq[ch] = 1 + charFreq.get(ch, 0)
        

    # our goal is to match all the characters from the 'charFreq' with the current window
    # try to extend the range [left, right]
    for right in range(len(string)):
        right_char = string[right]
        if right_char in charFreq:
        # decrement the frequency of matched character
            charFreq[right_char] -= 1
            if charFreq[right_char] == 0:
                matched += 1

        if matched == len(charFreq):
            return True

        # shrink the window by one character
        if right >= len(pattern) - 1:
            left_char = string[left]
            left += 1
            if left_char in charFreq:
                if charFreq[left_char] == 0:
                    matched -= 1
                charFreq[left_char] += 1

    return False

string = "oidbcaf"
pattern = "abc"
print(permutationsOfString(string, pattern))