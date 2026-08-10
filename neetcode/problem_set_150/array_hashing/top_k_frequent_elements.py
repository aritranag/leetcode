'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Input: nums = [7,7], k = 1
Output: [7]
'''


'''
Key Insight : Frequency maps for all characters, then sort the key,value pairs in descending by frequency and get the k most frequent pairs
Alternate (TODO) : Use a min heap to keep the k most frequent pairs, any time there is a frequency update, if it is greater than the min, modify the heap.
'''

def topKFrequent(nums : list[int], k: int) -> list[int]:
    # find out frequency of the ints in the array
    frequency = {}
    for i in nums:
        frequency[i] = frequency.get(i,0) + 1

    # now iterate through the entire hashmap and create a tuple in the form (elem,count)
    frequency_arr = []
    for i in frequency:
        frequency_arr.append((i,frequency[i]))

    # sort the array based on count
    frequency_arr = sorted(frequency_arr, key=lambda elem: elem[1], reverse=True)

    # now add the elems based on k
    result = []
    for i in range(0,k):
        result.append(frequency_arr[i][0])

    return result

# TODO : write a version using heap sort
# TODO : write a version using bucket sort

nums = [1,2,2,3,3,3]
k = 3
print(topKFrequent(nums,k))