"""
Given an array of strings strs, group the anagrams together. You can return the resultwer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once
"""
import collections
"""
Time: O(nmlog(m))
Space: O(n*m)
"""
def groupAnagrams(strings):
    results = {}
    for i in strings:
        x = "".join(sorted(i))
        if x in results:
            results[x].append(i)
        else:
            results[x] = [i]
    return list(results.values())

strings = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strings))

"""
Time: O(m*n) - where m is the total input strings given and n is the max length of those strings
Space: O(n*m)
"""
def groupAnagrams2(strings):
    result = collections.defaultdict(list)
        
    for s in strings:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result[tuple(count)].append(s)
    return list(result.values())


strings = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams2(strings))