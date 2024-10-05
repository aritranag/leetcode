import string

def checkInclusion(s1 : str, s2 : str) -> bool:
    """
    Checks whether any permutation of s1 is in s2
    Since it is given that s1 and s2 contains lowercase english letters, we will match frequency of letters in s1
    and every substring of length s1 in s2
    """
    flag = False

    # get mapping for s1
    s1Map = getInitialFrequency(s1)
    s1_frequency_str = getPermString(s1Map)

    #use sliding window method to compare frequency between substrings of length (s1) from s2
    window_length = len(s1)
    s2_length = len(s2)
    if window_length > s2_length:
        return flag
    else:
        curMap = getInitialFrequency(s2[0:0+window_length])
        for i in range(1,s2_length +1 - window_length):
            _frqStr = getPermString(curMap) # get the string representing the current frequency map
            if _frqStr == s1_frequency_str: # compare the strings, if match then set result to True and break
                flag = True
                break
            else:
                # modify the current map based on the characters being added and removed
                curMap[s2[i-1]] -= 1
                curMap[s2[i+window_length-1]] += 1
        
        # check for the last frequency map
        _frqStr = getPermString(curMap)
        if _frqStr == s1_frequency_str:
            flag = True
    return flag

def getInitialFrequency(s:str) -> dict:
    """
    Params:
        s : String for which the frequency distribution needs to be created.

    Result : 
        strMap : Frequency distribution for all characters in the string, if any character is not there, then the corresponding value will be 0.
                 This is to make the comparison between 2 dict's easy
    """
    res = {}
    # create initial mapping 
    for c in string.ascii_lowercase:
        res[c] = 0
    
    # populate the frequency map for the string
    for c in s:
        res[c] += 1

    return res

def getPermString(strMap : dict) -> str:
    """
    Get a string representation of the frequency mapping, will make it easier to compare
    """
    _fString = ""
    for k in strMap:
        if strMap[k] != 0:
            _fString += k + str(strMap[k])
    return _fString


s1 = "ab"
s2 = "eidbsaoba"

print(checkInclusion(s1,s2))