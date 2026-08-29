"""
Problem Description
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where:
1 <= index1 < index2 <= numbers.length
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
Examples
Example 1:
Input:
numbers = [2, 7, 11, 15], target = 9

Time 5 minutes

"""

def TwoSum(l1,target):
    left = 0;
    right = len(l1)-1

    while left<right:
        val = l1[left]+l1[right]
        if val==target:
            return [left,right]
        elif val<target:
            left+=1
        else:
            right-=1
    return []


print(TwoSum([2, 7, 11, 15],9))