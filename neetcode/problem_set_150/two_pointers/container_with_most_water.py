def maxArea(heights : list[int]) -> int:
    max_water = 0
    l,r = 0, len(heights)-1

    while l < r:
        water_area = min(heights[l],heights[r]) * (r-l)
        if water_area > max_water:
            max_water = water_area

        if heights[l] > heights[r]:
            r -= 1
        elif heights[l] <= heights[r]:
            l += 1
        
    return max_water


height = [2,2,2]
print(maxArea(height))
