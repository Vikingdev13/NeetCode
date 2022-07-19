"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
"""
Time: O(n)
Space: O(n)
"""
def dailyTemps(temps):
    # Initialize an empty stack and our solution stack with all 0's to begin with. 
    # For our stack, we'll be pushing pairs onto it, [indx, val]
    stack = []
    answer = [0] * len(temps)

    for indx, val in enumerate(temps):
        # while the stack is empty and the curr temp(val) is greater than the top [indx, val] of the stack
        while stack and val > stack[-1][0]:
            # We need to pop those pairs off the stack
            stackTemp, stackIndx = stack.pop()
            # Then we check how many indices we are from the last temp less than our current temp 
            answer[stackIndx] = (indx - stackIndx)
        # append the pair that is greater than the current val
        stack.append([val, indx])
    return answer


print(dailyTemps([73,74,75,71,69,72,76,73]))