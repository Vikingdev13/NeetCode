"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can't skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets
"""
"""
Time: O(n)
Space: O(1) - runs in constant space as there can be a maximum of three types of fruits stored in the hash map
"""
def fruits_into_baskets(fruits):
    start = maxLen = 0
    fruitFreq = {}

    for end in range(len(fruits)):
        right = fruits[end]
        if right not in fruitFreq:
            fruitFreq[right] = 1 + fruitFreq.get(right, 0)

        while len(fruitFreq) > 2:
            left = fruits[start]
            fruitFreq[left] -= 1
            if fruitFreq[left] == 0:
                del fruitFreq[left]
            start += 1
        maxLen = max(maxLen, (end - start + 1))
    return maxLen

fruits = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))