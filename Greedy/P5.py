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