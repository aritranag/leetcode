def trap(height: list[int]) -> int:

    if len(height) < 3:
        return 0
    
    # use two pointers
    l, r = 0, len(height)-1

    water_trapped = 0

    # find the first non zero height which has a lower height to the right of it
    while height[l] == 0 or height[l] < height[l+1]:
        l += 1
        if l == r:
            return 0
        

    # for the right, same idea, first non zero height which has a lower height to the left of it
    while height[r] == 0 or height[r] < height[r-1]:
        r -=1
        if r == l:
            return 0
        

    wall_length = 0
    while l < r:
        # compare between left and right height
        # if left one is smaller we will move the left pointer and keep the right 
        # for every movement, we will add as much water can be trapped = wall_length - min(h[l],h[r])
        # wall length only increases, otherwise stays the min between left and right side walls
        wall_length = max(wall_length,min(height[l],height[r]))
        
        if height[l] <= height[r]:
            water_trapped += max(wall_length - height[l],0)
            l += 1
        else:
            water_trapped += max(wall_length - height[r],0)
            r -= 1

    return water_trapped

# TODO : write the stack solution
# TODO : write the more elegant 2 pointer solution

height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height))