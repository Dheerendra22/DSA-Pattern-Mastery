def longestIncreasingSequence(nums): # TimeComplexiety O(2^n)
    n = len(nums)

    def LIS(index, prev, length):
        # Base case
        if index >= n:
            return length

        # Option 1: Skip current element
        skip = LIS(index + 1, prev, length)

        # Option 2: Take current element
        take = length

        if nums[index] > prev:
            take = LIS(index + 1, nums[index], length + 1)

        return max(take, skip)

    return LIS(0, float('-inf'), 0)

# l1 = [10,9,2,5,3,7,101,18] 
# print(longestIncreasingSequence(l1))

# improved Version of this

def longestIncreasingSequence(nums): # Time Complexiety O(n^2)
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n  # Initialize the dp array with 1s

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0


# l1 = [10,9,2,5,3,7,101,18] 
# print(longestIncreasingSequence(l1))

from collections import bisect

def longestIncreasingSequenceOptimized(nums): # Time Complexiety O(n log n)
    if not nums:
        return 0

    tail = []  # This will store the smallest tail of all increasing subsequences

    for num in nums:
        # Use binary search to find the index of the smallest number >= num
        # left, right = 0, len(tail)
        # while left < right:
        #     mid = (left + right) // 2
        #     if tail[mid] < num:
        #         left = mid + 1
        #     else:
        #         right = mid
        
        # we can also use this 
        left = bisect.bisect_left(tail, num) 
        # If left is equal to the length of tail, it means num is greater than all elements in tail
        if left == len(tail):
            tail.append(num)
        else:
            tail[left] = num  # Replace the existing value with num

    return len(tail)
l1 = [10,9,2,5,3,7,101,1] 
print(longestIncreasingSequenceOptimized(l1))

    
   