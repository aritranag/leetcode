1. Always consider building a hash set if possible
   - Be careful of string keys, they cost O(n) during first creation and avg O(n) during lookups
2. Strings are immutable in Python so, any string addition creates a new string -> O(n)
3. If you have to keep track of k-max or min element use a heap
