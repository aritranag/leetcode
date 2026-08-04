def twoSum(numbers : list[int],target:int) -> list[int]:
    # define 2 pointers from the beginning and the end
    # since the array is sorted, 
    # if the sum of the 2 numbers exceed the target, we decrease the sum by moving the pointer from the right
    # if the sum is smaller, then increase the pointer on the left
    # End the loop when the left meets or crosses the right pointer
    left, right = 0, len(numbers)-1
    result = []
    while left < right:
        if numbers[left] + numbers[right] == target:
            result = [left+1,right+1]
            break
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

    return result


def twoSumHashmap(numbers : list[int],target:int) -> list[int]:
    # store the values in map and check for complement
    num_map = {}
    for i, num in enumerate(numbers):
        _tmp = target - num
        if _tmp in num_map:
            return [num_map[_tmp],i+1]
        else:
            num_map[num] = i+1

    

numbers = [1,2,3,4]
target = 3
print(twoSumHashmap(numbers, target))