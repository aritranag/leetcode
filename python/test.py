def findKthBit(n: int, k: int) -> str:
    s = ["" for i in range(n)]
    s[0] = "0"

    for i in range(1,n):
        _invertS = invert(s[i-1])
        s[i] = s[i-1] + "1" + _invertS[::-1]
    
    return s[n-1][k-1]

def invert(s: str) -> str:
    res = ""
    # get the length of the string
    len_s = len(s)

    # generate a binary string of equal length with all 1s
    bin_comple = '0b' + '1'*len_s

    # make s binary string
    modified_s = '0b' + s

    # complement all bits using XOR
    result = int(modified_s,2) ^ int(bin_comple,2)

    return (bin(result)[2:]).zfill(len_s)


print(findKthBit(3,1))
print(findKthBit(4,11))