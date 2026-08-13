'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn)O(logn) time.

Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1
'''
def search(nums: list[int],target : int) -> int:
    left = 0
    right = len(nums)-1

    # base case, if the length of the array is 1, check the element
    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        return 0 if nums[0] == target else -1

    # for all other array lengths
    while left <= right:
        mid = left + ((right-left) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
        
    return -1

nums = [-1,3,4,5]
target = 5

print(search(nums, target))