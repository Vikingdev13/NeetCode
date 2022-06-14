"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
"""
Time: O(n)
Space: O(n)
"""
def topKFrequent(nums, k):
    table = {}
    freq = [[]for i in range(len(nums) + 1)]
    
    for num in nums:
        table[num] = 1 + table.get(num, 0)

    for num, count in table.items():
        freq[count].append(num)

    result = []

    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result
        
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))