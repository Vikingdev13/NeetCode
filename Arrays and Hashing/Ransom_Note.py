"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
"""
Time: O(n)
Space: O(1)
"""
import collections
def canConstruct(note, magazine):
    # if the ransom note contains more letters than the magazine, then there is no way the magazine can create the note
    if len(note) > len(magazine):
        return False
    # store the chars from magazine into a hashMap
    letters = collections.Counter(magazine)
    # iterate through the ransom note char by char
    for ch in note:
        # if the current char in note doesn't exist in the magazine, the note can't be constructed
        if letters[ch] <= 0:
            return False
        # decrement the char count from the magazine since we cant use it twice
        # EX: if we only have 2 'e' in the magazine, the note can only have 2 'e as well
        letters[ch] -= 1
    return True

note = "givemeallyourmoney"
magazine = "aeeegillmmnooruvyy"
print(canConstruct(note, magazine))