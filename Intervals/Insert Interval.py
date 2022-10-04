"""
Time: O(n)
Space: O(n)
"""
def insertInterval(intervals, newInterval):
    result = []

    for i in range(len(intervals)):
        # if the end val of newInterval is less than the start val of the current interval
        if newInterval[1] < intervals[i][0]:
            # insert the newInterval
            result.append(newInterval)
            # we know that all intervals that come after this are all non-overlapping
            # so we can just append the rest of the intervals
            return result + intervals[i:]
        # the start val of the newInterval is greater than the end val of the current interval
        elif newInterval[0] > intervals[i][1]:
            # then we'll just append the current interval
            result.append(intervals[i])
        # lastly, the newInterval is overlapping with the current interval
        else:
            # update the new interval(merge it)
            # take the min of the left val of both intervals and the max of the right val of both intervals
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    
    result.append(newInterval)
    
    return result

print(insertInterval([[1,3],[6,9]], [2,5]))                         # -> [[1,5],[6,9]]
print(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))    # -> [[1,2],[3,10],[12,16]]
