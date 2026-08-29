"""
Problem Description
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.
Example 1:
Input:
heights = [2,1,5,6,2,3]
Output:
10
Explanation: The above is a histogram where width of each bar is 1. 
The largest rectangle is shown in the red area, which has an area = 10 units (height 5, width 2).
"""


def solution(heights): #[2,1,5,6,2,3]
    stack=[]
    max_area=0
    heights.append(0) #[2,1,5,6,2,3,0]

    for i in range(len(heights)): # i=0 to 5
        while stack and heights[i]<heights[stack[-1]]:
            h = heights[stack.pop()]
            w =i if not stack else i - stack[-1]-1
            max_area =max (max_area,h*w)

        stack.append(i)
    return max_area

print(solution([2,1,5,6,2,3]))