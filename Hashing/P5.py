"""
Problem Description
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1
Input:
nums = [1, 1, 1], k = 2
Output:
2
Explanation:
The subarrays are [1, 1] (indices 0 to 1) and [1, 1] (indices 1 to 2).
Example 2
Input:
nums = [1, 2, 3], k = 3
Output:
2
Explanation:
The subarrays are [1, 2] and [3].
Constraints
1 <= nums.length <= 2 × 10⁴
-1000 <= nums[i] <= 1000
-10⁷ <= k <= 10⁷

"""


def CountSubarray(nums,k):
    count=0
    prefix_sum=0
    prefix_sum_dict={0:1}

    for num in nums:
        prefix_sum+=num 
        target=prefix_sum-k 

        if target in prefix_sum_dict:
            count+=prefix_sum_dict[target] 
        prefix_sum_dict[prefix_sum]=prefix_sum_dict.get(prefix_sum,0)+1
    return count
print(CountSubarray([3,4,7,2,-3,1,4,2,1],7))