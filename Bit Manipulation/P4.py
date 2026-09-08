"""
Problem Description

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Examples
Example 1:
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3]. 2 is the missing number in the range since it does not appear in nums.
"""
def findMissing(nums):
    Miss = len(nums)
    for i , n in enumerate(nums):
        Miss = Miss^(i^n)
    return Miss

print(findMissing([0,1,2,4]))