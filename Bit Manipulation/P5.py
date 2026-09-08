"""
Problem Description

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Examples
Example 1:
Input: n = 2
Output: [0, 1, 1]
Explanation:
0 → 0 (0 bits)
1 → 1 (1 bit)
2 → 10 (1 bit)

"""
def count1(n):
    count=0
    while n>0:
        count+=n&1
        n >>= 1
    return count
        
        
def solution1(n):
    ans = []
    for i in range(n+1):
        ans.append(count1(i))
    return ans
        
# print(solution(5))


# More Improved Version

def solution2(n):
    ans = [0]*(n+1)
    
    for i in range(1,n+1):
        ans[i]= ans[(i & (i-1))]+1
        
    return ans

print(solution2(5))
