"""
Given an array of strings strs, group the anagrams together. You can return the results in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once
"""
import collections
"""
Time: O(nlog(n)*Llog(L))
Space: O(n*L)
"""
def groupAnagrams(strings):
    # lambda func to sort each string by breaking them up into their characters, i.e 'eat' = ['a', 'e', 't']
    # strings will now be sorted/grouped by the strings with the same chars
    strings.sort(key = lambda word: str(sorted(word)))
    # initialize an empty result list and an empty currentGroup list
    # I will use the currentGroup list to keep track of strings that are the same and store them together
    # once I get to a string that isnt like the currentGroup, I will append the currentGroup to result,
    # then store the next string in currentGroup and reapeat process until all strings have been checked.
    result = []
    currentGroup = []

    for i in range(len(strings)):
        # append the current string to currentGroup
        currentGroup.append(strings[i])
        # make sure I'm not out of bounds, also check if the current sorted string is or isnt equal to the next sorted string
        if i == len(strings)-1 or sorted(strings[i]) != sorted(strings[i+1]):
            # if the current string is the same as the next string, keep moving
            # if the string is different, append what's currently stored in currentGroup to result, and
            # reset currentGroup to an empty list and repeat process
            result.append(currentGroup)
            currentGroup = []
    return result

strings = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strings))

"""
Time: O(nmlog(m))
Space: O(n*m)
"""
# def groupAnagrams2(strings):
#     results = {}
#     for i in strings:
#         x = "".join(sorted(i))
#         if x in results:
#             results[x].append(i)
#         else:
#             results[x] = [i]
#     return list(results.values())

# strings = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams2(strings))

# """
# Time: O(m*n) - where m is the total input strings given and n is the avg length of those strings
# Space: O(n*m)
# """
# def groupAnagrams3(strings):
#     # initialize an empty hashMap to be used to map character count to list of anagrams
#     # the following example sets the key as a tuple since in python lists cant be keys
#     # bc they're mutable, but the key is a tuple of character counts, and the values are the
#     # lists of the words that can be created using only those characters
#     # EX: key = (1:a,1:n,1:t) : ['ant','tan','nat']
#     result = collections.defaultdict(list)
#     # iterate through the input string    
#     for string in strings:
#         # count = 26 zeros to start, 1 for each character of the alphabet
#         count = [0] * 26
#         # iterate through every character of each input string
#         for ch in string:
#             # count the characters and map the characters to numbers 0-25
#             # a=0....z=25
#             # take ASCII val of current character and subract it from lowercase a, then increment that by 1
#             count[ord(ch) - ord('a')] += 1
#         # group all strings with same count together and append those strings to the output array
#         result[tuple(count)].append(string)
#     return list(result.values())


# strings = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams3(strings))