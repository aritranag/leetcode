def runningSum(nums):
    result = []
    running_sum = 0
    for num in nums:
        running_sum += num
        result.append(running_sum)

    return result


print(runningSum([3, 1, 2, 10, 1]))