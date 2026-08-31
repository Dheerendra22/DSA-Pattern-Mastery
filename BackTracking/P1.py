"""
Problem Description

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Examples
Example 1:

Input:

nums = [1,2,3]

Output:

[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Explanation:

For a set of size n, there are 2^n possible subsets.

In this case:

2^3 = 8

So, 8 subsets are generated.

Example 2:

Input:

nums = [0]

Output:

[[],[0]]
Constraints
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
def superSet(nums):
    if not nums:
        return []
    n = len(nums)
    result = []
    def subsets(i,r):
       result.append(r[:])
       for i in range(i,n):
           r.append(nums[i])
           subsets(i+1,r)
           r.pop()
    subsets(0,[])
    return result
nums = [1,2,3]
print(superSet(nums))

# Time Complexiety : O(n*2^n)
# space Complexiety : O(n)

        