def maximumSwap(num):
    s = str(num)
    l = [int(c) for c in s]
    result = []
    for i in range(0,len(l)):
        #if 0th index is largest in the rest of the array
        # add that to the result and continue
        if l[i] == max(l[i:]):
            result.append(l[i])
        # if not, find the maximum number, and its last index and swap with 0th index, 
        # then add the rest of the elements as is
        # and break
        else:
            temp = l[i:]
            max_num = max(temp)
            index_max = "".join([str(x) for x in temp]).rfind(str(max_num)) # joins into a string and uses rfind to find the last index of the max number found
            temp[0],temp[index_max] = temp[index_max],temp[0]
            result = result + temp
            break
    
    #join the result array into a string
    f_result = "".join([str(x) for x in result])
    return int(f_result,10)


assert maximumSwap(98368) == 98863
assert maximumSwap(2736) == 7236
assert maximumSwap(1993) == 9913
assert maximumSwap(193949) == 993941