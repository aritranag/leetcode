'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''

'''
Key Insight : Default is to divide (be careful of divide by zero)
Alternate : Use a prefix product and postfix product, to use a single array, first compute the prefix product and the loop from the end and keep on multiplying a running product and store the result in the appropriate place
'''

def productExceptSelf(nums : list[int]) -> list[int]:
    product = 1
    zero_count = 0

    for i in nums:
        if i != 0:
            product *= i
        else:
            zero_count += 1

    result = []
    if zero_count > 1:
        return [0]*len(nums)
    elif zero_count == 1:
        for i in nums:
            if i != 0:
                result.append(0)
            else:
                result.append(product)
    else:
        for i in nums:
            result.append(product//i)

    return result

def productExceptSelf_WithoutDiv(nums: list[int]) -> list[int]:
    result = [1]
    # compute the prefix product array
    for i in range(1,len(nums)):
        _val = nums[i-1] * result[i-1]
        result.append(_val)

    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] = result[i] * postfix
        postfix *= nums[i]

    return result


    

nums = [1,2,4,6]
print(productExceptSelf_WithoutDiv(nums))