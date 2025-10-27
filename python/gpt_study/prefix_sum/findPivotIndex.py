# Leetcode : 724
# Find Pivot Index -> Sum to the strict left of the index = sum to the strict right
def findPivotIndex(nums):
    total_sum = sum(nums)

    left_sum = 0

    # compare the left sum with the right sum
    # left sum = prefix sum - element 
    # right sum = total sum - element - left sum
    for i, num in enumerate(nums):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1


print(findPivotIndex([1,7,3,6,5,6]))
print(findPivotIndex([1,2,3]))
print(findPivotIndex([2,1,-1]))