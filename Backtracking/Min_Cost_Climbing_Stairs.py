"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""
"""
Time:
Space:
"""
def minCostClimbingStairs(cost):
    # append a 0 to the end of the array to simulate the top step
    cost.append(0)
    # iterate in reverse starting at the 3rd to last value of the array
    for i in range(len(cost)-3,-1,-1):
        # take the minimum value of jumping 1 or 2 stairs
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))