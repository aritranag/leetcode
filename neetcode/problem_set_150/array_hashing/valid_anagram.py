'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"
Output: true

Input: s = "jar", t = "jam"
Output: false
'''

'''
Key Insight : Create a frequency map and check for each character #FrequencyMap
Alternate : Exploit the fact that all chars are lower case and create an array of counts for all chars, positive for one string, negative for other
'''


# my Solution (uses less time)
def isAnagram(s : str, t: str):
    # first check length, if length is different, can't be anagram
    if len(s) != len(t):
        return False

    s_map,t_map = {},{}
    # create a dictionary of the both the strings
    for i in range(len(s)):
        if s[i] in s_map:
            s_map[s[i]] += 1
        else:
            s_map[s[i]] = 1

        # same for t
        if t[i] in t_map:
            t_map[t[i]] += 1
        else:
            t_map[t[i]] = 1

    # now compare the values for each key in the maps
    for k in s_map.keys():
        if (k not in t_map) or (s_map[k] != t_map[k]):
            return False

    return True


# optimal solution using constant space
def isAnagram_optimal(s : str, t: str):
    if len(s) != len(t):
        return False

    # define an array of length 26, since all the chars would be english lowercase alphabets
    # call lower on the strings as needed
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1 #ord will give the ascii value of the char, subtracting it 
        count[ord(t[i]) - ord('a')] -= 1 # we increment for chars in s, and decrement for chars in t. If they are anagram, final would be all 0

    result = not any(count) #will return True if any non 0 value is present

    return result

s = "abba"
t = "baab"
print(isAnagram_optimal(s,t))