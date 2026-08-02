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