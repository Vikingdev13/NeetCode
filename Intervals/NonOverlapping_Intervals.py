"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
"""
Time: O(nlog(n))
Space: O(1)
"""
def eraseOverlapIntervals(intervals):
    # sorting is O(nlog(n))
    intervals.sort()
    # store the first interval in a variable
    current = intervals[0]
    count = 0
    # iterate through the intervals beginning AFTER the first pair
    for interval in intervals[1:]:
        if interval[0] < current[1]:
            # if the current pair(0,1)'s 1 val is less than the 1 val of the interval, update the counter. 
            # This means that there is an overlap
            if interval[1] > current[1]:
                count += 1
            # else if the current pair(0,1)'s 1 val is greater than or equal to the intervals 1 val, 
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