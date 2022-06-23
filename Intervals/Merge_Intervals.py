"""
Given an array of intervals where intervals[i] = [start[i], end[i]], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input
"""
"""
Time: O(nlog(n))
Space: O(n)
"""
def mergeIntervals(intervals):
    # sort the intervals
    intervals.sort()
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
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            # else append the next interval
            result.append(interval)
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))