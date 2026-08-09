'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5

Constraints
1 <= tokens.length <= 10000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].
'''
def evalRPN(tokens: list[str]) -> int:
    import math
    operators = '+-*/'
    stack = []

    for t in tokens:
        if t not in operators:
            stack.append(int(t))
        elif t == '+':
            _val = stack.pop() + stack.pop()
            stack.append(_val)
        elif t == '-':
            _op2 = stack.pop()
            _op1 = stack.pop()
            stack.append(_op1 - _op2)
        elif t == '*':
            _val = stack.pop() * stack.pop()
            stack.append(_val)
        elif t == '/':
            _op2 = stack.pop()
            _op1 = stack.pop()
            stack.append(int(_op1/_op2))
        else:
            raise ValueError

    return stack.pop()


def evalRPN_recurse(tokens : list[str]) -> int:
    def recurse():
        token = tokens.pop()
        if token not in '+-*/':
            return int(token)

        right = recurse()
        left = recurse()

        if token == '+':
            return left + right
        elif token == '-':
            return left - right
        elif token == '*':
            return left * right
        elif token == '/':
            return int(left/right)

    return recurse()
        


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))

#10 * (6 / (9 + 3) * -11) + 17 + 5c