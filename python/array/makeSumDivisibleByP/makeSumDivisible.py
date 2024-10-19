def minSubarray1(nums: list[int], p: int) -> int:
    """
    Params:
        nums: List of integers from where the subarray needs to be found
        p : number by which the sum needs to be divisible

    Return:
        n : Length of the smallest subarray that can be removed to make the sum divisible (can be 0)/ -1 if such a thing is not possible
    """
    arraySum = sum(nums) # get the sum to check the divisibility
    flag = False
    min_output_length = len(nums)
    remainder = arraySum % p
    dividend = arraySum // p # get the dividend to make sure that there is a possible solution
    if remainder == 0:
        return 0
    elif dividend == 0: # if dividend is zero, divisor is greater than sum, so no solution is possible
        return -1
    else:
        start, end = 0,0 
        cur_sum = 0
        for i in range(0,len(nums)):
            if nums[i] == remainder: # if a single element can be removed that will always be the minimum possible answer
                flag = True
                min_output_length = 1
                break
            else:
                cur_sum = cur_sum + nums[i] # update the current sum and end index
                end = i
                if cur_sum == remainder:        
                    flag = True
                    if (end +1 - start) < min_output_length:
                        min_output_length = end +1 - start
                    start = end + 1 # +1 is done such that the next count will begin from the start of next element
                    cur_sum = 0
                elif cur_sum > remainder:
                    cur_sum -= nums[start]
                    start += 1
                
    if flag == True:
        return min_output_length
    else:
        return -1
    
def minSubarray(nums: list[int], p: int) -> int:
    total_sum = sum(nums)  # Calculate total sum of the array
    remainder = total_sum % p  # Find the remainder when total sum is divided by p

    # If the total sum is already divisible by p, return 0 (no subarray needs to be removed)
    if remainder == 0:
        return 0

    def find_smallest_subarray(nums, p, remainder):
        prefix_sum = 0
        min_length = len(nums)  # Initialize the minimum length of the subarray
        prefix_map = {0: -1}  # Store prefix sums modulo p with their indices

        for i, num in enumerate(nums):
            prefix_sum += num
            target_remainder = (prefix_sum % p - remainder) % p

            # If target_remainder exists in prefix_map, calculate subarray length
            if target_remainder in prefix_map:
                min_length = min(min_length, i - prefix_map[target_remainder])

            # Update prefix_map with the current prefix_sum % p
            prefix_map[prefix_sum % p] = i

        return min_length

    smallest_subarray_length = find_smallest_subarray(nums, p, remainder)
    return smallest_subarray_length if smallest_subarray_length < len(nums) else -1
    
# x = [26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]
# print(sum(x))
# print(sum(x)%26)
print(minSubarray([26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3],26))