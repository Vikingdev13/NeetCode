"""
Given an array of intervals where intervals[i] = [start[i], end[i]], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input
"""
"""
Time: O(nlog(n))
Space: O(n)
"""
def mergeIntervals(intervals):
    # sort the intervals, and use a lambda func to accept an argument pair, 
    # and return the value of pair[0], in other words, pair is a list and the 
    # lambda function will return the first element of the list. This allows 
    # us to sort the intervals based on the first element in each list
    intervals.sort(key = lambda pair : pair[0])
    # initialize result with the first interval after sorting
    result = [intervals[0]]

    # iterate through the intervals beginning with the second element, 
    # since we stored the first in result already
    for interval in intervals[1:]:
        # if the first pair, is less than or equal to the last element of the 
        # last interval in result [x,y] which is the y value compare it to the 
        # first element of that interval [x,y] so x, and update
        # EX: interval[0] = [2,6] and result[-1][1] = [1,3]
        # if the x value in interval[0] is less than the y value in result[-1][1]
        # then we merge them to create one interval, e.i [1,6]
        lastEnd = result[-1][1]
        if interval[0] <= lastEnd:
            lastEnd = max(lastEnd, interval[1])
        else:
            # else append the next interval
            result.append(interval)
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))