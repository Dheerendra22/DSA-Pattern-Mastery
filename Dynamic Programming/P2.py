def solution1(text1,text2): # Without dp
    m,n=len(text1),len(text2)
    def LCS(i,j):
        if i==m or j==n:
            return 0
        if text1[i]==text2[j]:
            return 1+LCS(i+1,j+1)
        else:
            return max(LCS(i+1,j),LCS(i,j+1))
    return LCS(0,0)
# print(solution1("abcde","fce"))
def solution2(text1,text2): # improve by dp that is apply Memorization in 2D array 
    m,n=len(text1),len(text2)
    mem=[[None for _ in range(n)] for _ in range(m)]
    
    def LCS(i,j):
        if i==m or j==n:
            return 0
        if mem[i][j] !=None:
            return mem[i][j]
        if text1[i]==text2[j]:
            mem[i][j]= 1+LCS(i+1,j+1)
        else:
            mem[i][j]= max(LCS(i+1,j),LCS(i,j+1))
        return mem[i][j]
    return LCS(0,0)
# print(solution2("abcde","ace"))
def solution3(text1,text2): #  bottom-up approach / tabulation method
    m,n=len(text1),len(text2)
    dp=[[0] *(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if text1[i]==text2[j]:
                dp[i+1][j+1]=1+dp[i][j]
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[m][n]
# print(solution3("abcde","ace"))
def solution4(text1,text2): # Most efficient logic Using DP
    if len(text1) <len(text2):
        text1,text2=text2,text1

    m,n=len(text1),len(text2)
    prev=[0]*(n+1)

    for i in range(m):
        current=[0]*(n+1)
        for j in range(n):
            if text1[i]==text2[j]:
                current[j+1]=1+prev[j]
                
            else:
                current[j+1]=max(prev[j+1],current[j])
        prev=current
    return prev[n]
#print(solution4("abcde","ace"))