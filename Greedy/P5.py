"""
Problem Description

You are given a string text consisting of lowercase English letters. Your task is to compress this string using Huffman Coding, a greedy algorithm used for lossless data compression.

In Huffman Coding:
Every unique character in the string is assigned a binary code.
The code must be a prefix code, meaning no code is a prefix of another (e.g., if 'a' is 0, 'b' cannot be 01).
To achieve maximum compression, characters that appear more frequently should have shorter codes, while less frequent characters have longer codes.

Return the minimum possible total length (number of bits) of the encoded string.

Example 1:

Input:

text = "aaabbc"

Output:

10
Explanation:

Frequencies:

a: 3
b: 2
c: 1

A possible Huffman Tree gives:

a: 0   (length 1)
b: 10  (length 2)
c: 11  (length 2)

Therefore, the total encoded length is:

a: 3 × 1 = 3 bits
b: 2 × 2 = 4 bits
c: 1 × 2 = 2 bits

Total = 3 + 4 + 2 = 9 bits
"""
import heapq
from collections import Counter 

def solution(text):
    if not text:
        return 0
    frequencies=Counter(text)

    if len(frequencies)==1:
        return len(text)
    
    heap=list(frequencies.values())
    heapq.heapify(heap)
    total_length=0

    while len(heap)>1:
        first=heapq.heappop(heap)
        second=heapq.heappop(heap)

        merged_weight=first+second 
        total_length+=merged_weight
        heapq.heappush(heap,merged_weight)
    return total_length


"""
k is the number of unique characters
n is the length of text
Time Complexity: O(n+klog k)
Space Complexity: O(k)

"""