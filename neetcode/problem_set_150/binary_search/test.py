def nearestMinSearch(nums : list[int],target : int) -> int:
    # find the index in nums <= target 
    # if all values in nums are greater than target then return -1
    if nums[0] > target:
        return -1
    elif nums[-1] < target:
        # all values are less than the target, return the last(max) one
        return len(nums)-1
    else:
        # value lies somewhere in between
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif mid + 1 < r and nums[mid+1] > target:
                return mid
            else:
                l = mid + 1
        return l

import bisect
nums = [1,2,3,5,16,17]
target = 0
idx_m = nearestMinSearch(nums,target)
idx = bisect.bisect_right(nums,target)
assert idx == idx_m+1, f"Mismatch idx_min = {idx_m},idx_bisect = {idx}"
