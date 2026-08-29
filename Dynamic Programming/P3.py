def solution1(nums): # by using Resursion 
    n=len(nums)
    def rob(n):
        if n==0:
            return 0
        if n==1:
            return nums[0]
        return max(rob(n-1),nums[n-1]+rob(n-2))
    return rob(n)

def robber(nums): # by using tablulation form bottom up approach
    n=len(nums)
    if not n:
        return 0
    if n ==1:
        return nums[-1]
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):
        
        dp[i] = max(nums[i]+dp[i-2],dp[i-1])
    return dp[-1]
# more efficient in terms of memory 
def robber(nums):
    n=len(nums)
    if not n:
        return 0
    if n ==1:
        return nums[-1]
    dp = [0]*2
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):
        
        current = max(nums[i]+dp[-2],dp[-1])
        dp[-2] = dp[-1]
        dp[-1] = current

    return dp[-1]


print(robber([2,7,9,3]))

    