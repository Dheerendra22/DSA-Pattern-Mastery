"""
Problem Description
You are given n items, each with a specific weight and a specific value. You are also given a knapsack that has a maximum weight capacity W.
You want to pack a subset of these items into your knapsack such that:

The total weight of the selected items does not exceed the capacity W.
The total value of the selected items is maximized.
Each item is unique and can be picked at most once (0/1 property).
Return the maximum total value that can be attained within the given weight capacity.

Examples
Example 1
Input:
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
Output:
220
Explanation:
If we pick items with weights 10 and 20, total value = 60 + 100 = 160.
If we pick items with weights 20 and 30, total value = 100 + 120 = 220.
If we pick items with weights 10 and 30, total value = 60 + 120 = 180.
The maximum value is 220.
Example 2
Input:
values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
W = 10
Output:
90
Explanation:
Pick items at index 1 (value 40) and index 3 (value 50).

Total weight:

4 + 3 = 7 <= 10
Total value:
40 + 50 = 90
Constraints
n == values.length == weights.length

1 <= n <= 1000

1 <= weights[i] <= 1000

1 <= values[i] <= 10^4

1 <= W <= 1000
This is the classic 0/1 Knapsack Dynamic Programming problem.

"""
def maxValue(values, weights, capacity):

    dp = [[0] * len(values) for _ in weights]

    def fun(v, w, c, i):

        # Base case
        if i == len(v) or c == 0:
            return 0

        # If current item cannot fit
        if w[i] > c:
            if not dp[i][i]:
             dp[i][i] = fun(v, w, c, i + 1)

            return dp[i][i]

        # Take or don't take current item
        dp[i][i] = max(
            v[i] + fun(v, w, c - w[i], i + 1),
            fun(v, w, c, i + 1)
        )
        return dp[i][i]

    return fun(values, weights, capacity, 0)


# values = [10, 40, 30, 50]
# weights = [5, 4, 6, 3]
# W = 10
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
#print(maxValue(values, weights, W))

# more better Solution
 
def Knapsack(val, w, cap):
   dp = [[0 for _ in range(cap+1)] for _ in range(len(val)+1)]
   for i in range(1,len(val)+1):
      for j in range(1,cap+1):
         if w[i-1]<=j:
           dp[i][j] = max(val[i-1]+dp[i-1][j-w[i-1]],dp[i-1][j])
         else:
            dp[i][j] = dp[i-1][j]
   return dp[len(val)][cap]

# values = [60, 100, 120]
# weights = [10, 20, 30]
# W = 50


# More improve version according to space complexiety

def knapsack(values,wt,cap):
   n = len(values)
   dp = [0]*cap+1

   for i in range(n):
      for w in range(cap,wt[i]-1,-1):
         dp[w]=max(dp[w],values[i]+dp[w-wt[i]])
   return dp[cap]
values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
W = 10
print(Knapsack(values,weights,W))