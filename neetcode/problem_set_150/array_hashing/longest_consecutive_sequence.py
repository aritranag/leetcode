def longestConsecutiveSequence(nums : list[int]) -> int:
    num_map = set(nums)
    # create a hashset of all the elems, 
    # for all elems in the set
    # if the elem-1 is in the set, then it is not the first elem
    # else it is the first elem of the sequence, 
    #   then we should iterate with elem+1 till we find a break and store the length if it is the longest sequence
    longest_sequence_len = 0
    for elem in num_map:
        if (elem-1) in num_map:
            continue
        else:
            sequence_len = 1
            t_elem = elem
            while (t_elem + 1) in num_map:
                sequence_len += 1
                t_elem += 1

            if sequence_len > longest_sequence_len:
                longest_sequence_len = sequence_len

    return longest_sequence_len
    
# TODO : look at the hash map solution

nums = []
print(longestConsecutiveSequence(nums))
