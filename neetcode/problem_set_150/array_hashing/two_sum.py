'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first. 

Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Input: nums = [4,5,6], target = 10
Output: [0,2]

Input: nums = [5,5], target = 10
Output: [0,1]
'''

'''
Key Insight : Iterate through the array and check for the complement (target - value), #HashMap
'''

def twoSum(nums : list[int], target : int):
    # nums : array of integers
    # target : 2 value in num must sum up to target
    # return -> index values that sums up to target, lowest first

    # create a hash map of the existing values in a single pass
    # check for the existence of the complement in the array, if complement exists then return the indices
    value_map = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in value_map:
            return [value_map[diff],i]
        value_map[n]= i


nums = [5,5]
target = 10

print(twoSum(nums,target))

