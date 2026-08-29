"""
Problem Description
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days
you have to wait after the i-th day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1
Input:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output:
[1, 1, 4, 2, 1, 1, 0, 0]
Example 2
Input:
temperatures = [30, 40, 50, 60]
Output:
[1, 1, 1, 0]
"""

def warmerDays(temperature):
    stack=[]
    warmtemp={}
    for i in range(len(temperature)):
        while stack and temperature[i] > stack[-1][0]:
            warmtemp[stack[-1][0]]=i-stack[-1][1]
            stack.pop()
        stack.append((temperature[i],i))

    return [warmtemp.get(num,0) for num in temperature]

print(warmerDays([73, 74, 75, 71, 69, 72, 76, 73]))

# More efficient version
def solution(temp):
    n=len(temp)
    answer=[0]*n
    stack=[]

    for i,current_temp in enumerate(temp):
        while stack and current_temp>temp[stack[-1]]:
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)
    return answer 

print(solution([73,74,75,71,69,72,76,73]))