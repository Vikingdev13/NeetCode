"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

"""
Time: O(n) - Since we will have to iterate through the entire input string

Space: O(n) - Since we're using a Stack, and might have to push the entire inoput string onto the Stack
"""

def validParentheses(s):
    # map closing brackets to open brackets
    brackets = {')' : '(', ']' : '[', '}' : '{'}
    # initialize empty stack
    stack = []
    # iterate through argument string
    for ch in s:
        # check if character(key) not in our hashMap
        if ch not in brackets:
            # if it is, push that character to the stack and continue on
            stack.append(ch)
            continue
        # if the stack is empty or the last character on the stack does not equal 
        # the current character of brackets, return False
        if not stack or stack[-1] != brackets[ch]:
            return False
        # else it does equal the current character of brackets and the stack 
        # is not empty, we pop it from the stack bc we have a match
        stack.pop()
    # return TRUE or FALSE that the stack is empty
    return not stack

s = '([)]'
print(validParentheses(s))