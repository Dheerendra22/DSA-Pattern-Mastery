def longestIncreasingSequence(nums):
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

l1 = [10,9,2,5,3,7,101,18] 
print(longestIncreasingSequence(l1))
