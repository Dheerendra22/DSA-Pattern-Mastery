"""
Problem Description
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
Examples
Example 1:
Input:
nums = [4,5,6,7,0,1,2], target = 0
Output:
4
Explanation:
The original array was [0,1,2,4,5,6,7]. It was rotated at index 4 (value 4). The target 0 is at index 4.
"""

def searchkey(nums,target):
    if not nums:
        return -1
    l=0
    r=len(nums)-1

    while l<=r:
        mid = l + (r-l)//2
        if nums[mid]==target:
            return mid

        if nums[l]<=nums[mid]:
            if nums[l]<=target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        if nums[mid+1]<nums[r]:
            if nums[mid+1]<=target<=nums[r]:
                l= mid+1
            else:
                r=r-1

    return -1
print(searchkey([8,9,0,1,2,7],0))
