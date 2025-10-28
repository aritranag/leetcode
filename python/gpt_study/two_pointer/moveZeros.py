# Leetcode 283: Move Zeros
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def moveZeros(nums):


    # find the first zero element
    for i, num in enumerate(nums):
        if num == 0:
            pointer_l = i
            break

    # iterate from the next element and move them to the right
    for i in range(pointer_l+1,len(nums)):
        #print(nums,pointer_l,i)
        if nums[i] != 0:
            nums[pointer_l],nums[i] = nums[i],nums[pointer_l] # swap the numbers
            pointer_l += 1
        

moveZeros([0,0,1,3,12])


