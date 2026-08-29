"""
Problem Description
You have some number of ropes with different lengths. You need to connect these ropes into one single rope. The cost to connect two ropes is equal to the sum of their lengths.
You want to connect all the ropes such that the total cost is minimized. Return the minimum total cost of connecting all the given ropes.
Example 1
Input:
ropes = [2, 4, 3]
Output:
14
Explanation:
Connect ropes 2 and 3 (cost = 5). Now ropes are [5, 4].
Connect ropes 5 and 4 (cost = 9). Now there is only one rope.
Total cost = 5 + 9 = 14.
Note that if we connected 2 and 4 first (cost = 6), then 6 and 3 (cost = 9), the total cost would be 15.
Example 2
Input:
ropes = [1, 8, 3, 5]
Output:
30
Explanation:
Connect 1 and 3 (cost = 4). Ropes: [4, 8, 5].
Connect 4 and 5 (cost = 9). Ropes: [9, 8].
Connect 9 and 8 (cost = 17).
Total cost = 4 + 9 + 17 = 30.
Constraints
1 <= ropes.length <= 10^4
1 <= ropes[i] <= 10^4
"""
import heapq
def RopeSum(l1):
    if not l1:
        return 0
    minheap=[]
    for num in l1:
        heapq.heappush(minheap,num)

    first = heapq.heappop(minheap)
    total_cost=0
    while minheap:
        second=heapq.heappop(minheap)
        cost=first+second
        total_cost += cost 
        first=cost
    return total_cost

print(RopeSum([1, 8, 3, 5]))
        
"""
Time Complexiety O(nlogn)
space Complexiety O(n)
"""