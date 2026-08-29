"""
Problem Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
i != j, i != k, and j != k
and
nums[i] + nums[j] + nums[k] == 0
Notice that the solution set must not contain duplicate triplets.
Examples
Example 1:
Input:
nums = [-1, 0, 1, 2, -1, -4]
Output:
[[-1, -1, 2], [-1, 0, 1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.

nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
"""
def triplet(l1):
    if len(l1)< 3:
       return set()
    
    result = set()
    l1= sorted(l1)
    k=len(l1)-1
    while(k>1):
        i=0 
        j=k-1
        while(i<j):
            if l1[i]+l1[j] == -(l1[k]):
                result.add(tuple(sorted([l1[i], l1[j], l1[k]])))
                i+=1
                j-=1
            elif l1[i]+l1[j] < -(l1[k]):
             i+=1
            else:
               j-=1

        k-=1    

    return result
print(triplet([-1, 0, 1, 2, -1, -4]))
