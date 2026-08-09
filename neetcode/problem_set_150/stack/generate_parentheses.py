'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Input: n = 1
Output: ["()"]

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
def generateParenthesis(n : int) -> list[str]:
    # we try to do a depth first search, each step, we either add '(' or ')'
    paren_set = set()
    stack = []
    def recurse(open, close):
        if open == close == n:
            paren_set.add(''.join(stack))
            return

        # check for the number of open 
        if open < n:
            stack.append('(')
            recurse(open+1,close)
            stack.pop()

        # check for number of close, which has to be less than open
        if close < open:
            stack.append(')')
            recurse(open,close+1)
            stack.pop()

    recurse(0,0)
    return list(paren_set)
    

# TODO : Write the DP solution

print(generateParenthesis(3))