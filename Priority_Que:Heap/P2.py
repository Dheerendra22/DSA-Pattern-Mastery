"""
=================== Find K most frequent Elements ================

Problem Description
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input:
nums = [1,1,1,2,2,3], k = 2
Output:
[1,2]

Example 2:
Input:
nums = [1], k = 1
Output:
[1]

Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""

import heapq
from collections import Counter

def mostFrequent(l1, k):

    freq = Counter(l1)

    minheap = []

    for value, frequency in freq.items():
        heapq.heappush(minheap, (frequency, value))

        if len(minheap) > k:
            heapq.heappop(minheap)

    return [v for f, v in minheap]

print(mostFrequent([3,1,3,1,3,1,2,2,3], 2))

