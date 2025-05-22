
# 21st May 2025 
def zeroArrayTransformation(nums: list[int],queries:list[list[int]]):
    n = len(nums)
    
    # Initializing a difference array to calculate the prefix sum
    freq = [0]* (n+1)

    # Step 1: Mark the range in the difference array
    for l, r in queries:
        freq[l] += 1
        if r + 1 < n:
            freq[r + 1] -= 1

    if freq[0] < nums[0]:
        return False

    # Step 2: Convert to prefix sum to get how many times each index is covered
    for i in range(1, n):
        freq[i] += freq[i - 1]
        if freq[i] < nums[i]:
            return False

    # Step 3: Check if each number can be decremented to 0, is combined to the previous step to make it faster
    # for i in range(n):
    #     if freq[i] < nums[i]:
    #         return False

    return True


nums = [7]#[4,3,2,1]
queries = [[0,0]]#[[1,3],[0,2]]

print(zeroArrayTransformation(nums, queries))