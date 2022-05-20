"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input
"""
"""
Time: O(nlog(n))
Space: O(n)
"""
def mergeIntervals(intervals):
    # sort the intervals, and use a lambda func to accept and argument pair, 
    # and return the value of pair[0], in other words, pair is a list and the 
    # lambda function will return the first element of the list. This allows 
    # us to sort the intervals based on the first element in each list
    intervals.sort(key = lambda pair : pair[0])
    # initialize result with the first interval
    result = [intervals[0]]

    # iterate through the intervals beginning with the second element, 
    # since we stored the first in result already
    for interval in intervals[1:]:
        # if the first element of interval, so in [x,y], this is looking at x, is less than 
        # or equal to the last element of the last interval in result [x,y] which is the y value
        # compare it to the first element of that interval [x,y] so x and update
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            # else append the next interval
            result.append(interval)
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))