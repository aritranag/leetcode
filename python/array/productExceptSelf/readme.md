# 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Additional Case**  
Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

### Examples

---

Example 1:

Input: nums = [1,2,3,4]  
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]  
Output: [0,0,9,0,0]

## Tags - Array, 2 Pointers.

## Solution

**Naive(v1)**

1. Reverse the array and store it. `[4,3,2,1]`
2. Create 2 extra arrays of the same length as the given array. Initialize the first elements to 1, since the first element doesn't have a prefix and the last element does not have a suffix. `[1],[1]`
3. The first array, lets call it **from_start**, stores the product prefixes of each element in the array.  
   `from_start[i] = product of nums till [i-1] `  
   `from_start = [1,1,2,6]`
4. The second array, lets call it **from_end**, stores the product suffixes of each element. To calculate the product suffix,the reverse array is used. The actual calculation also calculates the prefixes of the reverse order array, thus only performing 1 multiplication at each step.  
   `from_end[i] = product of nums till [i-1] in the reverse array`
   `from_end = [1,4,12,24]
5. Each element of the final answer array is essentially a product of its prefix and suffix. This is computed as follows:  
   `final_arr[i] = from_start[i] * from_end[len(arr) - 1 - i]`

   This is done in this way because essentially for any element i, from_start[i] contains the product prefix of the element, but the product suffix is stored in from_end[len(arr) - 1 - i]. Eg:  
   `final_arr[2] = prefix(num[0] * num[1]) * suffix(num[3])`  
   `final_arr[2] = from_start[2] * from_end[4-2-1] = 2 * 4 = 8`

**Optimized(v2)**

1. We use only O(1) extra space here, by essentially storing the prefix product and the suffix product in 2 variables.
2. The time saving observation is that there is no need to make 2 passes through the array, 2 pointers working from 2 ends of the array will give the same result.
3. In every step, the prefix product calculated till that point is multiplied with the suffix product till that point.
   `[,,,x,,,](position i) => (product prefix till x) * (product suffix from x)`
