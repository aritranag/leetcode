'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Input: s = "[]" Output: true

Input: s = "([{}])" Output: true

Input: s = "[(])" Output: false
'''
def isValidParentheses(s : str) -> bool:
    stack = []
    flag = True
    paren_dict = {'(' : ')', '{' : '}' , '[' : ']'} # map of open and closing parens
    for char in s:
        if char in paren_dict: # checks only for the keys which is hte opening parens
            stack.append(char)
        elif char in ')}]':
            if len(stack) > 0:
                _c = stack.pop()
                if paren_dict[_c] == char:
                    continue
                else:
                    return False
            else:
                return False

    if len(stack) > 0:
        return False
    return True

s = "()[{}]"
print(isValidParentheses(s))

