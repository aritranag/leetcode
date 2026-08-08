def lengthOfLongestSubstring(s: str) -> int:
    # sliding window technique
    # window starts from beginning, we extend the window by 1 for each non repeating char found in the valid substring
    # if we find a repeating char we move the left side only till the index of the repeating char
    # every time a repeating char is found we check for the length of the string found
    # check at the end for the substring finishing at the last
    l,r = 0,0 # keeps track of the window instead of actually creating an array
    max_length = 0
    char_set = {}
    for i,char in enumerate(s):
        if char in char_set and char_set[char] >= l:
            # check the length of the current window and store the length if it is the max
            if (r-l) > max_length:
                #final_string = s[l:r]
                max_length = r - l

            # find the index of the repeating char
            _i = char_set[char]

            # set the left side to the index + 1 to only consider indexes in the new substring
            l = _i+1

        # increase the right position
        r += 1
        # store the index of the character found
        char_set[char] = i
            

    # compare for the last window
    if (r - l) > max_length:
        #final_string = s[l:r]
        max_length = r - l

    #print(final_string)
    return max_length

# TODO : write optimal solution for sliding window

s="dvdf"
print(lengthOfLongestSubstring(s))