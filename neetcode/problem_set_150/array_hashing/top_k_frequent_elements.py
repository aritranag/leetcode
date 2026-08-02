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