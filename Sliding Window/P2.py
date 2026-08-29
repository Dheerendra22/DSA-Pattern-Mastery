"""
Problem Description
Given a string s, find the length of the longest substring without repeating characters.
A substring is a contiguous sequence of characters within a string.
Examples
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

def longestSubstring(str):
    maxlength=0
    start=0
    window=""
    for end in range(len(str)):
        if str[end] in window:
            while str[end] in window:
                window = window[1:]
                start+=1
            
        window=window+str[end]
        maxlength = max(maxlength,len(window))
    return maxlength

print(longestSubstring("abacbdbc"))


# Standard Approach to solve the Problem !!

def length_of_longest_substring(s):
    char_map={}
    left=0
    max_length=0

    for right in range(len(s)):
        current_char=s[right]

        if current_char in char_map and char_map[current_char]>=left:
            left=char_map[current_char]+1

        char_map[current_char]=right

        current_window_size=right-left+1
        max_length=max(max_length,current_window_size)
    return max_length

print(length_of_longest_substring("abacbdbc"))