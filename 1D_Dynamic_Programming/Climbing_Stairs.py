"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
"""
Time: O(n)
Space: O(1)
"""
def climbStairs(n):
    one, two = 1, 1

    for _ in range(n - 1):
        tmp = one
        one = one + two
        two = tmp
    return one


if __name__ == "__main__":
    n = 3
    print(climbStairs(n)) # 3 ways to climb
    n = 2
    print(climbStairs(n)) # 2 ways to climb
    n = 5
    print(climbStairs(n)) # 8 ways to climb