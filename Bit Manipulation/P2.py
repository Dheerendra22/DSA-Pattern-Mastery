"""
Problem Description

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Examples
Example 1

Input:

nums = [1, 2, 3]

Output:

[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
Example 2

Input:

nums = [0]

Output:

[[], [0]]
"""

def solution(nums):
    n=len(nums)
    output=[]

    for i in range(1<<n):
        subset=[]
        for j in range(n):
            if (i>>j)&1:
                subset.append(nums[j])
        output.append(subset)
    return output

print(solution([1,2,3]))
# Time Complexity O(n.2^n)
# Space Complexity O(n)