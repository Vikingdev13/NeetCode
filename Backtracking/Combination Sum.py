"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
"""
Time:
Space:
"""
def combinationSum(candidates, target):
    result = []


    def dfs(indx, current, total):
        if total == target:
            # we want to append a copy of current, not current itself since we want to continue to use the variable/list and not have to worry about resetting it each time we use it
            result.append(current.copy())
            return
        
        if indx >= len(candidates) or total > target:
            return

        current.append(candidates[indx])
        dfs(indx, current, total + candidates[indx])
        current.pop()

        dfs(indx + 1, current, total)

    dfs(0, [], 0)
    return result

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target)) # -> [[2,2,3],[7]]