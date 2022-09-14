"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
"""
Time: O(n)
Space: O(1)
"""
def climbStairs(n):
    if n == 1:
        return n

    a, b = 1, 2
    for _ in range(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b

print(climbStairs(5))