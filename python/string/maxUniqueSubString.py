def maxUniqueSplit(s: str) -> int:
    i = maxSplit(s,[])
    return i

def maxSplit(s: str, subStrinArr: list):
    """
    Greedily creates substrings using minimum number of chars, if gets stuck, returns -1 and tries again
    """
    if len(s) == 0:
        # base case, if the remaining string is empty
        return 0
    else:
        #length of the string > 1, check for the minimum length to make unique
        # and that the rest to be valid
        result = 1
        sub_len = 1
        while result != 0:
            temp = s[:sub_len]
            if (temp in subStrinArr):
                sub_len += 1
                continue 
            subStrinArr.append(s[:sub_len])
            result = maxSplit(s[sub_len:],subStrinArr)
            if result != 0:
                subStrinArr.pop()
                sub_len += 1
            else:
                break
    return len(subStrinArr)


print(maxUniqueSplit('a'))