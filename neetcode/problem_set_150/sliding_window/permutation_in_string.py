'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Input: s1 = "abc", s2 = "lecabee"
Output: true (The substring "cab" is a permutation of "abc" and is present in "lecabee".)

Input: s1 = "abc", s2 = "lecaabee"
Output: false

1 <= s1.length, s2.length <= 10000
'''

def checkPermutation(s1 : str, s2 : str) -> bool:

    # base case check
    if len(s2) < len(s1):
        return False
    elif len(s1) == 0:
        return False

    # Substring of s2 will have to contain a permutation of s1
    # create a freqquency map of s1
    frq_s1 = {}
    for c in s1:
        frq_s1[c] = frq_s1.get(c,0) + 1

    # now take the first s1 chars in s2 and create a frequency map out of them
    frq_w = {}
    window_size = len(s1)
    for c in s2[:window_size]:
        frq_w[c] = frq_w.get(c,0) + 1

    # compare the frequency maps to see if a permutation of s1 lies in the window
    flag = True
    for k in frq_s1:
        if k not in frq_w or frq_s1[k] != frq_w[k]:
            flag = False
            break

    if flag is True:
        return True
    else:
        # initiate a loop and check for all windows from 1 to s2-s1
        for i in range(1,len(s2) - window_size + 1):
            _flag = True
            # adjust the frq map of the window, 
            # decrease the count for the char at i which is no longer in the window, 
            # add the count for char at i+window_size - 1 which is now part of the window now
            frq_w[s2[i-1]] -= 1
            frq_w[s2[i+window_size - 1]] = frq_w.get(s2[i+window_size - 1],0) + 1

            # compare the frequency maps of s2 and the window, if issue found, break with Flag = false
            for k in frq_s1:
                if k not in frq_w or frq_s1[k] != frq_w[k]:
                    _flag = False
                    break

            # Flag is True till the end, which means the maps are same and a permutation of s2 is in the window
            if _flag is True:
                return True

    return False

# TODO : write the sliding window variant with array comparisons
            
s1 = "ace"
s2 = "lecaabee"
print(checkPermutation(s1,s2))