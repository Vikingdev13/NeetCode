"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
"""
Time: 
Space:
"""
"""
*** My initial thought process for this was to use a stack in a similar method to the valid parentheses problem. My initial implementation had some bugs and I couldn't wuite get it right. I looked up the solution to see what I was missing. I was missing counters to keep track of the open and close braces. Basically, whatever the value of n, we multiply it by 2 since parentheses come in pairs. So then I needed to 
"""
def generateParenthese(n):
    stack = []
    result = []
    
    def backtrack(openCount, closedCount):
        if openCount == closedCount == n:
            result.append("".join(stack))
            return 
        
        if openCount < n:
            stack.append("(")
            backtrack(openCount + 1, closedCount)
            stack.pop()
            
        if closedCount < openCount:
            stack.append(")")
            backtrack(openCount, closedCount + 1)
            stack.pop()
            
    backtrack(0,0)
    return result

print(generateParenthese(3))