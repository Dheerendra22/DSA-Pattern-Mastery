"""
Problem Description
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
The string will only contain lowercase English letters.
Example 1
Input: s = "assassination"
Output: 9
Explanation: The character 't' at index 9 is the first character that does not occur at any other index.
Example 2
Input: s = "poppins"
Output: 1
Explanation: The character 'o' at index 1 is the first character that does not occur at any other index.
Example 3
Input: s = "aabb"
Output: -1
"""
def nonRepeatingCharacter(strs):
    d = {}
    duplicate = set()

    for i in range(len(strs)): # O(n)
        key = strs[i]

        if key in d:
            duplicate.add(key)
        else:
            d[key] = i

    for key, index in d.items():
        if key not in duplicate:
            return index

    return -1
print(nonRepeatingCharacter("assassination"))

#. more compact code or other Version 
def nonRepeatingCharacter(s):
    count_map={}
    for ch in s:
        count_map[ch]=count_map.get(ch,0)+1
    
    for index in range(len(s)):
        if count_map[s[index]]==1:
            return index 
    return -1

print(nonRepeatingCharacter('assassination'))