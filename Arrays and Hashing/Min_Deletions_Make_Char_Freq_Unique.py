"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""
"""
Time: O(n)
Space: O(1) - it's constant since at most there will be 26 chars in the array
"""
import collections
def minDeletions(str):
    # initialize a dictionary to store the char with their frequency counts
    count = collections.Counter(str)
    # initialize an empty set that we will use to store the frequency counts we've seen
    seen = set()
    # result will keep count of the number of deletions we've made
    result = 0
    # iterate over the values of the dictionary
    for freq in count.values():
        # make sure that the current freq is in the seen set and is greater than 0
        # we don't care if a char has a freq below 0
        while freq in seen and freq > 0:
            # decrement the freq count if it's already in the seen set and increment the result to account for a deletion
            freq -= 1
            result += 1
        # we add a freq when it's not in the set already
        seen.add(freq)
    return result

print(minDeletions("aab"))      # -> 0
print(minDeletions("aaabbbcc")) # -> 2
print(minDeletions("ceabaacb")) # -> 2