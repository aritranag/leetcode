def productExceptSelf_v1(nums):
    '''
    Naive version (v1)
    Uses 2 arrays to store the prefix and the suffix for all numbers
    Final solution is a product of the values from 2 ends
    '''
    nums_reverse = nums[::-1]
    nums_length = len(nums)
    final_arr = []

    from_start = [1]
    from_end = [1]

    for i in range(1,nums_length):
        from_start.append(from_start[i-1] * nums[i-1])
        from_end.append(from_end[i-1] * nums_reverse[i-1])
    
    for i in range(nums_length):
        final_arr.append(from_start[i] * from_end[nums_length-1-i])
    
    return final_arr


nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
print(productExceptSelf_v1(nums2))