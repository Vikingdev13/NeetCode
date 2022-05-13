"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
"""


"""
*** 2 pointer/Sliding window approach ***
Time: O(n)
Space: O(1)
"""
def buySellStocks(prices):
    # initialize pointers left to the first element and right the the second element of array
    left, right = 0,1
    maxProfit = 0
    # iterate the right pointer across array until the end
    while right < len(prices):
        # check the values of the left pointer and the right pointer
        # if the val at the left is less than the val at the right
        # update the profit and maxProfit
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        # else the val at the left is GREATER than the val at right
        # in which case we move the left to the val of the right pointer
        # then increment the right pointer
        # EX: for the given array, left = 7 and right = 1
        # this would mean that we bought the stock at 7 and try to sell at 1, which is -6 profit and silly :)
        else:
            left = right
        right += 1    
    return maxProfit

prices = [7,1,5,3,6,4]
print(buySellStocks(prices))