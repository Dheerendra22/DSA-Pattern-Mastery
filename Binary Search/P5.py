"""
Problem Description
You are given an array of integers stalls, which represents the locations of stalls on a straight line. You are also given an integer k, representing the number of aggressive cows you need to assign to these stalls.
Your task is to assign each of the k cows to a stall such that the minimum distance between any two cows is as large as possible.
Return the maximum possible minimum distance.
Examples
Example 1:
Input: stalls = [1, 2, 8, 4, 9], k = 3
Output: 3
Explanation: One optimal way to place the 3 cows is at positions 1, 4, and 9.
Distance between 1 and 4 is 3.
Distance between 4 and 9 is 5.
The minimum distance is min(3, 5) = 3. No other arrangement provides a minimum distance greater than 3.
"""


def solution(stalls,k):
    stalls.sort()
    def canPlaceCows(m): # m is min distance 
        count=1 
        pos=stalls[0]

        for i in range(1,len(stalls)):
            if stalls[i]-pos >=m:
                count+=1
                pos=stalls[i]

            if count>=k:
                return True 
        return False 
    l,r=0,stalls[-1]-stalls[0]
    result=0
    while l<=r:
        m=l+(r-l)//2
        if canPlaceCows(m):
            result=m 
            l=m+1
        else:
            r=m-1 
    return result 

print(solution([10,1,2,7,5],3))