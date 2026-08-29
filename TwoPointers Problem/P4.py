"""
Problem Description
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k. To get accepted, you need to do the following things:

Modify the array nums such that the first k elements of nums contain the unique elements in the order they were initially present in nums. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer
                               // with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;

for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
Examples
Example 1:
Input:
nums = [1, 1, 2]

"""

def RemoveDuplicates(l1):
    if not l1:
        return 0
    k=1
    i=0
    j=i+1
    while j<len(l1):
        if l1[i] != l1[j]:
           i+=1
           l1[i]=l1[j]
           j+=1
           k+=1
        else:
            j+=1

    return k

lis = [0,0,1,1,1,2,2,2,3,3,4,4]

k = RemoveDuplicates(lis)

print(lis,k)

    
