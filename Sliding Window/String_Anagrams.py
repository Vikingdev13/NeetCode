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

string = "abbcabc"
pattern = "abc"
print(find_string_anagrams(string, pattern))