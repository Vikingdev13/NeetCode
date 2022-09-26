"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
"""
"""
Time: O(m+n)
Space: O(m)
"""
def find_string_anagrams(string, pattern):
  left, matched = 0, 0
  charFreq = {}

  for chr in pattern:
    if chr not in charFreq:
      charFreq[chr] = 0
    charFreq[chr] += 1

  result = []
  # Our goal is to match all the characters from the 'charFreq' with the current window
  # try to extend the range [left, right]
  for right in range(len(string)):
    right_char = string[right]
    if right_char in charFreq:
      # Decrement the frequency of matched character
      charFreq[right_char] -= 1
      if charFreq[right_char] == 0:
        matched += 1

    if matched == len(charFreq):  # Have we found an anagram?
      result.append(left)

    # Shrink the sliding window
    if right >= len(pattern) - 1:
      left_char = string[left]
      left += 1
      if left_char in charFreq:
        if charFreq[left_char] == 0:
            # Before putting the character back, decrement the matched count
            matched -= 1
        # Put the character back  
        charFreq[left_char] += 1  

  return result
    # string_len, pattern_len = len(string), len(pattern)
    # if string_len < pattern_len:
    #     return []

    # res = []
    # # stores the frequency of each character in the pattern string
    # pattern_counter = [ 0 ] * 26
    # # stores the frequency of each character in the current window
    # window = [ 0 ] * 26
    # a = ord('a')  # ascii value of 'a'
    # # first window
    # for i in range(pattern_len):
    #     pattern_counter[ord(pattern[i]) - a] += 1
    #     window[ord(string[i]) - a] += 1
    # if window == pattern_counter:
    #     res.append(0)

    # for i in range(pattern_len, string_len):
    #     window[ord(string[i - pattern_len]) - a] -= 1
    #     window[ord(string[i]) - a] += 1
    #     if window == pattern_counter:
    #         res.append(i - pattern_len + 1)
    # return res


string = "cbaebabacd"
pattern = "abc"
print(find_string_anagrams(string, pattern))