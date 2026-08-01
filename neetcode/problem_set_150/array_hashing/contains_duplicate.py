def has_duplicate(nums: list[int]):
    result_set = set()
    for num in nums:
        if num in result_set:
            return True
        else:
            result_set.add(num)
    return False


print(has_duplicate([1,2,3,4]))