# 2044 :Count Number of Maximum Bitwise-OR Subsets

def countMaxOrSubsets(nums: list[int]) -> int:
    """
    Params:
        nums: List of numbers

    Return:
        num : count of the number of subsets with the maximum bitwise OR
    """
    _bitWiseSum = 0
    for elem in nums:
        _bitWiseSum |= elem




print(countMaxOrSubsets([1,2,3]))