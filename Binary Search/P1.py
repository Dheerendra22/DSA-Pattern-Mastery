"""
Problem Description
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Examples
Example 1:
Input:
nums = [-1,0,3,5,9,12], target = 9
Output:
4
Explanation:
9 exists in nums and its index is 4.
"""
def search(nums,target):
    if not len(nums):
        return -1
    if target<nums[0] or target>nums[-1]:
        return -1
    left=0
    right=len(nums)-1
    while left<right:
        mid = left + (right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
            

    return -1

print(search([-1,0,3,5,9,12],9))