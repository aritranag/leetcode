'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time


Input: nums = [3,4,5,6,1,2]
Output: 1

Input: nums = [4,5,0,1,2,3]
Output: 0

Input: nums = [4,5,6,7]
Output: 4
'''


def findMin(nums: list[int]) -> int:
    # Finding the pivot element and finding the min element for a rotated sorted array are the same thing
    # property to leverage, if num[middle] > num[right], then pivot is in the right half, else left

    l,r = 0, len(nums)-1

    while l<r:
        middle = l + (r-l)//2
        if nums[middle] > nums[r]:
            l = middle + 1
        else:
            r = middle

    return nums[l]


nums = [7,8,1,2,3,4,5,6]
print(findMin(nums))
