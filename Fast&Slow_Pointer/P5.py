"""
Problem Description
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Examples
Example 1:
Input: n = 19
Output: true
Explanation:
1² + 9² = 1 + 81 = 82

8² + 2² = 64 + 4 = 68

6² + 8² = 36 + 64 = 100

1² + 0² + 0² = 1
"""

def solution(n):
    def get_next(num):
        total=0
        while num>0:
            digit=num % 10
            total = total + digit**2
            num = num//10
        return total 
    
    slow=n
    fast=get_next(get_next(n))
    while fast !=1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast==1

print(solution(19))