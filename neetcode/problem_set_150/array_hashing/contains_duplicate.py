'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Input: nums = [1, 2, 3, 3]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false
'''

'''
Key Insight : Create a hash set of values and check if the value is already in the set, Hash Set
'''

def has_duplicate(nums: list[int]):
    result_set = set()
    for num in nums:
        if num in result_set:
            return True
        else:
            result_set.add(num)
    return False


print(has_duplicate([1,2,3,4]))