def twoSum(nums : list[int], target : int):
    # nums : array of integers
    # target : 2 value in num must sum up to target
    # return -> index values that sums up to target, lowest first

    # create a hash map of the existing values
    value_map = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in value_map:
            return [value_map[diff],i]
        value_map[n]= i


nums = [5,5]
target = 10

print(twoSum(nums,target))

