"""
Problem Description
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
Example 1:
Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output:
[3, 3, 5, 5, 6, 7]

"""
import heapq
def max_in_sliding(l1,k):
    if len(l1)<k :
        return []
    maxheap=[(-l1[i],i)for i in range(k)]
    heapq.heapify(maxheap)
    result= [-maxheap[0][0]]

    for i in range(k,len(l1)):
        heapq.heappush(maxheap,(-l1[i],i))

        while maxheap[0][1]<=i-k:  # if mAX element not in current sliding window
            heapq.heappop(maxheap)
    

        result.append(-maxheap[0][0])

    
    
    return result

print(max_in_sliding([1, 3, -1, -3, 5, 3, 6, 7],3))

