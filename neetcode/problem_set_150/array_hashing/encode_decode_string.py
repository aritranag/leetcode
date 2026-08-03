def encode(strs: list[str]) -> str:
    
    if len(strs) == 0:
        return ""
    else:
        final_string = ""
        for string in strs:
            str_len = len(string)
            final_string += str(str_len) + "$" + string

    return final_string


def decode(s : str) -> list[str]:
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