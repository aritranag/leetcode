# Trapping Rain Water
# 3 Sum
# Longest Repeating Character Replacement
# Daily Temperatures

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # works with the idea of a stack, of checking from the end
    result = [0] * len(temperatures)
    n = len(temperatures)

    max_temp = 0
    # start from the end and move towards the beginning
    for i in range(n-1,-1,-1):
        if temperatures[i] >= max_temp:
            max_temp = temperatures[i]
            result[i] = 0
        else:
            j = i+1
            while j<n:
                if temperatures[i] < temperatures[j]:
                    result[i] = j-i
                    break
                else:
                    j = j+result[j]

    return result


def threeSum(nums: list[int]) -> list[list[int]]:
    # 2 pointers

    # sorting at the beginning will arrange the array in ascending order
    nums.sort()
    res = set()

    i = 0
    while i < len(nums) and nums[i] <= 0:
        # now initialize j and k (from the left of i and from the end)
        j = i+1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                res.add((nums[i],nums[j],nums[k]))
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1


        i += 1

    # convert to list of lists
    result = []
    for val in res:
        result.append(list(val))

    return result


def characterReplacement(s: str, k: int) -> int:

    # for each uppercase character, identify the longest substring if we are only replacing with that character
    res = 0

    # create a set of the unique chars
    frequency = set(s)

    # iterate through the chars already present and check the longest window for them
    for c in frequency:
        left, right = 0,0
        count = 0
        while right < len(s):
            if s[right] == c:
                count += 1

            if (right + 1 - left) - count <= k:
                right += 1
            else:
                res = max(right - left,res)
                left += 1
                if s[left-1] == c:
                    count -= 1
        res = max(right - left,res)

    return res




def trapRainWater(height: list[int]) -> int:
    # 2 pointers solution
    # at ith position there can only be water = min(max height to the left, max height to the right) - height at i
    leftMax, rightMax = height[0],height[-1]
    l,r = 0, len(height)-1
    water_trapped = 0
    while l < r:
        if leftMax < rightMax:
            # left wall is shorter, then move the left pointer
            l += 1
            leftMax = max(leftMax,height[l])
            water_trapped += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            water_trapped += rightMax - height[r]

    return water_trapped


height = [0,2,0,3,1,0,1,3,2,1]
print(trapRainWater(height))

# nums = [0,1,0]
# print(threeSum(nums))

# s = "XYYX"
# k = 2
# print(characterReplacement(s,k))

#temperatures = [42,42,40]
#print(dailyTemperatures(temperatures))
