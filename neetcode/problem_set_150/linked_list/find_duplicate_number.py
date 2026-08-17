'''
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
There is exactly one repeated integer in nums, and every other integer appears at most once.
Return the repeated integer.

Input: nums = [1,2,3,2,2]
Output: 2

Input: nums = [1,2,3,4,4]
Output: 4
'''
def findDuplicate(nums: list[int]) -> int:
    seen = set()
    for val in nums:
        if val in seen:
            return val
        else:
            seen.add(val)

nums = [1,2,3,4,4]
print(findDuplicate(nums))