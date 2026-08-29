"""
Problem Description
Given an array of points where points[i] = [xᵢ, yᵢ] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance:
For the sake of this problem, you can compare the squared distances (x² + y²) to avoid the square root operation.
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
Example 1
Input:
points = [[1,3],[-2,2]], k = 1
Output:
[[-2,2]]
"""
import heapq

def nearToOrigin(points,k):
    maxheap=[]
    for index, (x, y) in enumerate(points):
        square = -(pow(x,2)+pow(y,2))
        if len(maxheap)<k:
            heapq.heappush(maxheap,(square,index))
        elif square > maxheap[0][0]:
            heapq.heapreplace(maxheap,(square,index))

    result = []
    for _ in range(k):
        square,index = heapq.heappop(maxheap)
        result.append(points[index])
    return result

print(nearToOrigin([[3,3],[5,-1],[-2,4]],2))

