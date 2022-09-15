"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""
"""
Time: O(nlog(n)) - since we have to sort
Space: O(n) - Timsort, which is Python's built in sorting algo uses worst case O(n) space 
since it basically creates a new list under the hood.
"""
def meetingRooms(intervals):
    # sort the input
    intervals.sort()
    # iterate through input starting at the index 1
    for i in range(1, len(intervals)):
        # i1 will start off withe the [x,y] at the index 0
        # i2 will start off with the [x,y] at index 1
        i1 = intervals[i-1]
        i2 = intervals[i]
        # compare the last val(y) of i1 to the first val(x) of i2
        # if it's larger, the nthere is an overlap and you can just return False
        # since you can't attend a meeting that starts while you're still in one
        if i1[1] > i2[0]:
            return False
    return True

print(meetingRooms([[7,10],[2,4]]))             # -> True
print(meetingRooms([[0,30],[5,10],[15,20]]))    # -> False
print(meetingRooms([[0,30],[60,240],[90,120]])) # -> False

# Using a Heap
# Time: O(nlog(n))
# Space: O(1)
import heapq
def meetingRoomsHeapify(intervals):
    heapq.heapify(intervals)
    currMax = 0

    while intervals:
        start, end = heapq.heappop(intervals)
        if start < currMax:
            return False
        else:
            currMax = max(currMax, end)
    return True

print(meetingRoomsHeapify([[7,10],[2,4]]))             # -> True
print(meetingRoomsHeapify([[0,30],[5,10],[15,20]]))    # -> False
print(meetingRoomsHeapify([[0,30],[60,240],[90,120]])) # -> False

