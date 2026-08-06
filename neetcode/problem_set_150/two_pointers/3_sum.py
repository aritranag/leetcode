def threeSum(nums:list[int]) -> list[list[int]]:
    # First lets sort the array
    nums = sorted(nums)

    result = []
    # Fix the left number and then use 2 pointers to find the other two
    for i, a in enumerate(nums):

        # if a is greater than zero, then everything to its left is already positive and hence does not need to be checked
        if a > 0:
            break

        # skip duplicates for a
        if i > 0 and a == nums[i-1]:
            continue

        # initialize the pointers 
        l,r = i+1, len(nums) - 1

        # for each number we will only loop through until l < r
        while l < r:
            threeSum = a + nums[l] + nums[r]
            # if three sum > 0, we need to move the pointer of the right, since the sum is too big, else move the pointer from the left
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                # threeSum is zero, which means it is a valid triplet
                result.append([a,nums[l], nums[r]])
                l += 1
                r -= 1
                # skip duplicates for the left pointer which is basically the middle value 
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return result

# TODO : write the hashmap solution

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(threeSum(nums))



        