"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
"""
"""
Time: O(n)
Space: O(n)

*** My thought process for this one was to use a stack. When we encounter a digit, just push it onto the stack. If we encounter an operator, we need to use that operator on the previous 2 digits, then push that result to the stack. Once finished, there should only be the result of all the arithmetic and we return that.

"""
def evalRPN(tokens):
    stack = []

    for ch in tokens:
        if ch == "+":
            stack.append(stack.pop() + stack.pop())
        elif ch == "-":
            ch1, ch2 = stack.pop(), stack.pop()
            stack.append(ch2 - ch1)
        elif ch == "*":
            stack.append(stack.pop() * stack.pop())
        elif ch == "/":
            ch1, ch2 = stack.pop(), stack.pop()
            stack.append(int(ch2 / ch1))
        else:
            stack.append(int(ch))
    return stack[0]


tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

