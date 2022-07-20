"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""
"""
Time: O(n*log(m)) let n = len of input and m = num of bananas in a pile
Space: O(1)
"""
import math

def minEatingSpeed(piles, h):
    # initialize our boundaries
    left, right = 1, max(piles)
    # initialize our result to the max value or the array since we know that at a max, this value will work
    result = right

    while left <= right:
        # get the middle value of our boundaries
        # hours is the total hour Koko spends
        k = (left+right)//2
        hours = 0

        # iterate over the piles and calculate the the hour/s spent
        for pile in piles:
            # we need to round up
            hours += math.ceil(pile/k)
        # Check if the middle val is a workable speed, if not adjust search area by half
        if hours <= h:
            result = min(result, k)
            right = k - 1
        else:
            left = k + 1
    return result

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))