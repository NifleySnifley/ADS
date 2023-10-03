## Chapter 2

### Exercises
1. O(n2)
2. O(n)
3. O(log(n))
4. O(n3)
5. O(n)
6. The list indexing operation is O(1) due to the fact that python’s implementation of lists stores items in the list at addresses in memory that can be easily derived in O(1) time from the index of an item in the list. A simple “experiment” to prove this would be to create a benchmark test similar to the ones used by the book’s authors. This sort of test would also be applicable to Exercise 7
7. See above
8. See above
9. Implemented in [exercises.py](exercises.py)
10. Yes, sort-of. Using a variation of an algorithm such as counting sort, it is possible to have a runtime less than n log n, but the time complexity depends on the range of the values in the array and since the bound of the values in the array is not mentioned in the exercise, I don’t think it’s smart to rely on it being within a reasonable range. Anyways, I have implemented an algorithm in [exercises.py](exercises.py) using this strategy with a worst-case runtime of O(n+k) where k is the range of the array, but it uses O(k) spare memory.
