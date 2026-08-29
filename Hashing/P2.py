"""
Problem Description
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input:
strs = ["eat","tea","tan","ate","nat","bat"]
Output:
[["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input:
strs = [""]
Output:
[[""]]
Example 3:
Input:
strs = ["a"]
Output:
[["a"]]
Constraints
1 <= strs.length <= 10⁴
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
from collections import Counter
def countAnagrams(strs):
    count=0
    d = {}
    for s in strs:
        key = tuple(sorted(Counter(s).items()))
        d.setdefault(key, []).append(s)

    return [d.values()]

print(countAnagrams(["eat","tea","tan","ate","nat","bat"]))

# implemented by Saurab Sir
def solution1(words): # O(N.KlogK)
    d1={}
    for word in words:
        key=''.join(sorted(word)) 
        d1[key]=d1.get(key,[])+[word]
    return list(d1.values())

def solution2(words): # O(N.K)
    d1={}
    for word in words:
        count=[0]*26
        for ch in word:
            index=ord(ch)-ord('a')
            count[index]+=1
        key=tuple(count)
        d1[key]=d1.get(key,[])+[word]
    return list(d1.values())

print(solution2(["aet","eat","steam","tea","teams"]))