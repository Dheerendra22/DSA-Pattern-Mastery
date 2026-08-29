"""
Problem Description
Given an array of integers nums and a positive integer k, find the maximum sum of any contiguous subarray of size k.
A subarray is a contiguous non-empty sequence of elements within an array.
Examples
Example 1:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray [5, 1, 3] has the maximum sum of 9.
Example 2:
Input: nums = [2, 3, 4, 1, 5], k = 2
Output: 7

"""

def sumOfSubArray(arr,k):
    maxSum = 0
    window = maxSum
    start = 0
    for end in range(len(arr)):
        window+=arr[end]

        if end>=k-1:
            if end>k-1:
                window-=arr[start]
                start+=1
            if maxSum<window:
                    maxSum=window

    return maxSum

print(sumOfSubArray([2, 1, 5, 1, 3, 2],3))

