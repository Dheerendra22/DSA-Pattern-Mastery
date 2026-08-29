"""
Problem Description
Given a word txt and a pattern pat, find the total count of all anagrams of pat in txt.
An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "abcd" and "dabc" are anagrams of each other.
A substring of txt is considered an anagram of pat if the characters in the substring can be rearranged to form pat.
Examples
Example 1:
Input:
txt = "forxxorfxdofr", pat = "for"
Output:
3
Explanation:
Substring "for" at index 0 is an anagram.
Substring "orf" at index 5 is an anagram.
Substring "ofr" at index 9 is an anagram.
"""


from collections import Counter
def checkAnagrams(txt,pat):
    window=""
    count=0
    for end in range(len(txt)):
        if len(window)<len(pat):
            window = window+txt[end]
            continue
        elif Counter(window) == Counter(pat):
                count+=1

        window = window[1:] + txt[end]

    if Counter(window) == Counter(pat):
        count += 1
    return count
        
            
print(checkAnagrams("aabaabaa","aaba"))


# Standard way of code 

def solution(txt,pat):
    n=len(pat)
    left=0
    count=0
    d1={}
    for ch in pat:
        d1[ch]=d1.get(ch,0)+1
    d2={}
    #txt = "forxxorfxdofr", pat = "for"
    for right in range(len(txt)):
        d2[txt[right]]=d2.get(txt[right],0)+1

        if right>=n-1:
            if d1==d2:
                count+=1
            d2[txt[left]]-=1
            if d2[txt[left]]==0:
                del d2[txt[left]]
            left+=1
    return count
print(solution("forxxorfxdofr","forx"))

