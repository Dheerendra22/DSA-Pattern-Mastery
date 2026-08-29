
"""
Problem Description
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
Examples
Example 1:
Input:
s = "ADOBECODEBANC", t = "ABC"
Output:
"BANC"
Explanation:
The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""


from collections import Counter
def solution(s,t):
    if not s or not t or len(s)<len(t):
        return ""
    dict_t=Counter(t)
    required=len(dict_t)

    l,r=0,0

    window_counts={}
    formed=0

    ans=float("inf"),None,None

    while r < len(s):
        ch=s[r]
        window_counts[ch]=window_counts.get(ch,0)+1

        if ch in dict_t and window_counts[ch]==dict_t[ch]:
            formed+=1
        
        while l<=r and formed==required:
            ch=s[l]

            if r-l+1 <ans[0]:
                ans=(r-l+1,l,r)

            window_counts[ch]-=1
            if ch in dict_t and window_counts[ch]<dict_t[ch]:
                formed -=1

            l+=1
        r+=1
    return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]

print(solution("ADOBECODEBANC","ABC"))