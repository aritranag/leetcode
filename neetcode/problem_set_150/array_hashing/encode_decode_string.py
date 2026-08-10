'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
'''

'''
Key Insight : Counting the chars in a string and putting the length before the string will allow to encode any string. Put a delimiter between the length and the start and make sure to read till the delimter since the length can be more than 1 character
'''

def encode(strs: list[str]) -> str:
    # for encoding add the string length and a special char to denote its end
    if len(strs) == 0:
        return ""
    else:
        final_string = ""
        for string in strs:
            str_len = len(string)
            final_string += str(str_len) + "$" + string

    return final_string


def decode(s : str) -> list[str]:
    # find the length till the special char and then extract the string based on the length
    if s == "":
        return []

    result = []
    while len(s) > 0:
        str_len_end = s.find('$') # end of the length encoding

        str_len = int(s[:str_len_end]) # length of the string
        result.append(s[str_len_end + 1:str_len_end + str_len+1]) # get the substring and append it

        s = s[str_len_end + str_len + 1: ] # iterate on the rest

    return result




strs = ["",""]
encoded_str = encode(strs)
print(encoded_str)
print(decode(encoded_str))