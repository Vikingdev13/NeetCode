"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
# Heap Solution
"""
Time: O(k*log(n)) if k < n and O(n) if k = n which is better than O(nlog(n))
Space: O(n+k)
"""
from collections import Counter
import heapq

def topKFreqHeap(nums, k):
    if k == len(nums):
        return nums

    # build the hashMap
    count = Counter(nums)
    # build heap of top k elements and convert it to an array
    return heapq.nlargest(k, count.keys(), key=count.get)

nums = [1,1,1,2,2,3]
k = 2
print(topKFreqHeap(nums,k))

# Optimal Solution
"""
Time: O(n)
Space: O(n)
"""
def topKFrequent(nums, k):
    # initialize an empty dict and a list comp of empty lists, the same len of our input array
    table = {}
    freq = [[]for i in range(len(nums) + 1)]
    # iterate through the input array and put the val and its count into the dict table
    for num in nums:
        table[num] = 1 + table.get(num, 0)
    # now iterate through the dict and append each val at the index of its count
    # EX: input array has three 1's, so we will place a 1 at the third index in freq and so on
    for num, count in table.items():
        freq[count].append(num)
    # initialize out result list
    result = []
    # now we will iterate through the freq array backwards
    for i in range(len(freq)-1,0,-1):
        # for each val in freq, we will append it to the result array
        for val in freq[i]:
            result.append(val)
            # once the result array is of size k, we stop adding to it and return it
            if len(result) == k:
                return result
        
print(topKFrequent(nums, k))