# Time Complexity O(nxn!)
# Space Complexity O(n)
def permutation(nums): 
    n=len(nums)
    result=[]
    def perm(i):
        if i==n:
            result.append(nums[::])
            return
        for j in range(i,n):
            nums[i],nums[j]=nums[j],nums[i]
            perm(i+1)
            nums[i],nums[j]=nums[j],nums[i]
    perm(0)
    return result 
for l in permutation([1,2,3,4]):
    print(l)