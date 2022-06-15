"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
"""
Time: O(nlog(n))
Space: O(1)
"""
def eraseOverlapIntervals(intervals):
    # sorting is O(nlog(n))
    # using [[1,2],[2,3],[3,4],[1,3]] as a test
    # the intervals look like this now [[1,2], [1,3], [2,3], [3,4]]
    intervals.sort()
    # store the first interval in a variable
    # current = [1,2]
    current = intervals[0]
    count = 0
    # iterate through the intervals beginning AFTER the first pair
    # starting at [1,3], [2,3], [3,4]
    for interval in intervals[1:]:
        # if interval[0] which is [1,3] 0 = 1 is less than current[1] which is [1,2] 1 = 2 which is TRUE
        if interval[0] < current[1]:
            # if interval[0] 0 = 1 > current[1] 1 = 2, which is FALSE, move to the next interval
            if interval[1] > current[1]:
                count += 1
            # else if interval[1] is less than or equal to current[1], 
            # set the current pair's 0 val to the intervals 1 val and update the counter since there was an overlap
            elif interval[1] <= current[1]:
                current = interval
                count += 1
        # else there is no overlap
        else:
            current = interval
    return count
            

intervals = [[1,2],[2,3],[3,4],[1,3]]
# intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))