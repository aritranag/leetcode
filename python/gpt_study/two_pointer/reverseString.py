# Leetcode 344 : Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
def reverseString(s):
    # Use 2 pointers from opposite direction
    slow, fast = 0,len(s)-1

    while slow < fast:
        s[slow], s[fast] = s[fast], s[slow]
        # Move the pointers towards each other
        slow += 1
        fast -= 1
    
    return s

input = ["H","a","n","n","a","h"]
print(reverseString(input))



