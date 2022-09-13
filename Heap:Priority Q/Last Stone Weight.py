"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
"""
Time:
Space:
"""
import heapq
# use a MaxHeap, but python doesn't have a MaxHeap, have to use a minHeap for implementation
def lastStoneWeight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        # get the 2 largest stones, so pop off the largest first, 
        # then the next largest will move to top and pop second
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        # since we made all the values in the heap negative in order to utilize a MaxHeap
        # we have to reverse the operator to compare first and second
        if second > first:
            # since we're storing neg vals, subtract the smallest by the largest and 
            # it'll give us a neg val to push back into the heap 
            heapq.heappush(stones, first - second)
    # edge case for no stones left
    # push a 0 into the heap
    stones.append(0)
    return abs(stones[0])

    


stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))