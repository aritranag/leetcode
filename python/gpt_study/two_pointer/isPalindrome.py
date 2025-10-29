# Leetcode 125 : Valid Palindrome
'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''
def isPalindrome(s:str):
    # Remove non-alphanumeric characters and convert to lowercase
    alphanumeric_chars = "".join(c for c in s if c.isalnum()).lower()

    slow, fast = 0, len(alphanumeric_chars) - 1

    while slow < fast:
        if alphanumeric_chars[slow] != alphanumeric_chars[fast]:
            return False
        else:
            slow += 1
            fast -= 1
    
    return True


s = "race a car"
print(isPalindrome(s))