'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Input: nums = [3,5,6,0,1,2], target = 4
Output: -1
'''


'''
Key Insight : For a rotated sorted array, find the pivot using the property that middle > right implies the right half has the pivot else left
            After finding the pivot it is 2 sorted arrays of left, pivot and pivot+1,right
            For Binary search problems in general, the array has to be sorted, so if we can get a sorted array, we can perform bsearch quickly
'''

def search(nums:list[int],target: int) -> int:

    def bsearch(nums, left, right, target):
        while left <= right:
            middle = left + ((right-left)//2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    # property of the rotated sorted array - if it is not fully sorted then one half will violate the property left < middle < right
    # once we identify which half we can then perform normal binary search
    left, right = 0, len(nums)-1

    while left <= right:
        middle = left + (right-left)//2

        if nums[middle] == target:
            return middle

        # now check for the whole array, if it is sorted
        if (nums[left] <= nums[middle] <= nums[right]):
            # array is fully sorted, perform normal binary search
            return bsearch(nums, left, right, target)

        # if left half is sorted
        if nums[left] <= nums[middle]:
            if nums[left] <= target <= nums[middle]:
                return bsearch(nums, left, middle, target)
            else:
                left = middle + 1
                continue
        else:
            # right half is sorted, so check the details there
            if nums[middle] <= target <= nums[right]:
                return bsearch(nums, middle, right, target)
            else:
                right = middle - 1

    return -1


nums = [1]
print(search(nums, 1))