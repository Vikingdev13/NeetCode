"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
"""
Time: O(n)
Space: O(1)
"""
def climbStairs(n):
    if n < 2:
        return n
    one, two = 1, 2

    for _ in range(3, n + 1):
        third = one + two
        one = two
        two = third
    return two


if __name__ == "__main__":
    n = 1
    print(climbStairs(n)) # 1 way to climb
    n = 3
    print(climbStairs(n)) # 3 ways to climb
    n = 2
    print(climbStairs(n)) # 2 ways to climb
    n = 5
    print(climbStairs(n)) # 8 ways to climb