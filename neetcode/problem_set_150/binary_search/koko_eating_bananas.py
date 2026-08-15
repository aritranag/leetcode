'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Input: piles = [1,4,3,2], h = 9
Output: 2

Input: piles = [25,10,23,4], h = 4
Output: 25
'''

'''
Key Intuition : Find an upper bound, then run binary search till the upper bound to identify the lower bound. 
                Ensure we also search the case, where l == r and we only keep track of the min valid solution till far
'''

def minEatingSpeed(piles : list[int], h:int) -> int:
    import math
    # base case - if h == piles of bananas, then find the max number and return, since koko has to eat 1 pile per hour
    pile_count = len(piles)
    if h == pile_count:
        return max(piles)

    # upper bound of the answer, if koko eats this in 1 hour, then he can always finish
    upper_bound = max(piles)

    # now we run a binary search from 1 to upper_bound to identify the answer
    l, r = 1, upper_bound

    solution = upper_bound #default answer is the upper bound, we will make it as low as possible
    while l <= r:
        k = l + (r-l)//2

        res = 0
        # check for all values in the pile
        for val in piles:
            res += math.ceil(val/k)
            if res > h:
                break

        if res > h: # this is not a valid solution since time being taken is greater than allotted, which means we need to increase the k
            l = k + 1
        else: # this is a valid solution, so, we check whether this is the min found so far, if yes, we store it and then try to find a lower value if possible
            solution = min(solution,k)
            r = k - 1

    return solution

piles = [25,10,10,4]
h = 6
print(minEatingSpeed(piles,h))