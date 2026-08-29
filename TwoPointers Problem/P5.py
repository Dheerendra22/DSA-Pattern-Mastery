"""
Problem Description
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
A palindrome is a string that reads the same backward as forward.
Examples
Example 1:
Input: s = "aba"
Output: true
Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

"""

def checkPalimdrone(str):
    def check(i,j):
        while i<j:
            if str[i]!=str[j]:
                        return False
            else:
                 i+=1
                 j-=1

        return True

    i=0
    j=len(str)-1
    while i<j:
        if str[i]!=str[j]:
            return check(i+1,j) or check(i,j-1)
        else:
            i+=1
            j-=1

    return True

print(checkPalimdrone("abca"))