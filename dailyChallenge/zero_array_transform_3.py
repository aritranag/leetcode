
def zero_array_transform_max_removal(nums: list[int], queries:list[list[int]]):

    maxNum = max(nums)
    n = len(nums)
    query_len = len(queries)

    # sort the list of queries by length of the interval
    queries.sort(key=lambda x: x[1] - x[0],reverse=True)

    # initialize the difference array
    diff = [0] * (n+1)

    # iterate maxNum of times, if possible
    if maxNum <= query_len:
        for i in range(maxNum):
            li, ri = queries[i]

            # increment the left index
            diff[li] += 1
            diff[ri+1] -= 1

        # calculate the prefix sum
        for i in range(1,n+1):
            diff[i] += diff[i-1]
        
        # subtract each entry from the original 
        for i in range(n):
            nums[i] = max(nums[i] - diff[i],0)
        
        # iterate through the rest of the entries one by one to check when the list becomes zero
        
        for final_val in range(maxNum,query_len):
            if any(nums) > 0:
                li, ri = queries[final_val]
                for j in range(li,ri+1):
                    nums[j] = max(nums[j] - 1,0)
            else:
                break
        
        if final_val < query_len:
            return query_len - final_val
        else:
            if any(nums) > 0:
                return -1
            else:
                return 0
    else:
        return -1
    

nums = [1,2,3,4]#[2,0,2]#[1,1,1,1]#[2,0,2]
queries = [[1,3],[0,2],[1,2],[1,3]]#[[0,2],[0,2],[1,1]]
queries.sort(key=lambda x: x[1] - x[0],reverse = True)
print(queries)
#print(zero_array_transform_max_removal(nums,queries))

