"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
"""
Time: O(n*2^n)
** since the amount of subsets of any array will be 2^n, where n is the len of the array, the time will always be n*2^n
Space: O(n)
"""
def subsets(nums):
    result = []
    # global array for use inside dfs function
    subset = []
    def dfs(indx):
        if indx >= len(nums):
            result.append(subset.copy())
            return
        # decision to include nums[indx]
        subset.append(nums[indx])
        # recursive call on the next element
        dfs(indx + 1)

        # decision NOT to include nums[indx]
        subset.pop()
        dfs(indx + 1)
    dfs(0)
    return result
        

nums = [1,2,3]
print(subsets(nums)) # -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]