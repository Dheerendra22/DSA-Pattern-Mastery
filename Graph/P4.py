"""
Problem Description
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words:
beginWord -> s₁ -> s₂ -> ... -> sₖ

such that:

Every adjacent pair of words differs by a single letter.
Every sᵢ for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sₖ == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
Examples
Example 1:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output:
5
Explanation:
One shortest transformation sequence is:

"hit" -> "hot" -> "dot" -> "dog" -> "cog"
which is 5 words long.

"""

# from collections import deque # Brute force Approach

# def is_similar(word1, word2):
#     count = 0

#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1

#     return count == 1


# def wordLadder(beg,end,wordlist):
#     if end not in wordlist:
#         return 0
#     n = len(wordlist)
#     visited = [0]*n
  
#     queue=deque([(beg,1)])

#     while queue:
#         word,length = queue.popleft()

#         for i,w in enumerate(wordlist):
#             if is_similar(word,w) and not visited[i]:
#                 queue.append((w,length+1))
#                 visited[i]=1
#             elif word == end:
#                 return length
#             else:
#                 pass

#     return 0

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# print(wordLadder(beginWord,endWord,wordList))

# MySirG code 

from collections import deque 
def solution(beginWord,endWord,wordList):
    word_set=set(wordList)
    if endWord not in word_set:
        return 0
    
    L=len(beginWord)

    all_combo_dict={}
    for word in wordList:
        for i in range(L):
            intermediate_word=word[:i]+"*"+word[i+1:]
            if intermediate_word not in all_combo_dict:
                all_combo_dict[intermediate_word]=[]
            all_combo_dict[intermediate_word].append(word)
    
    queue=deque([(beginWord,1)])

    visited={beginWord}
    while queue:
        current_word,length=queue.popleft()
        for i in range(L):
            intermediate_word=current_word[:i]+"*"+current_word[i+1:]

            if intermediate_word in all_combo_dict:
                for word in all_combo_dict[intermediate_word]:
                    if word==endWord:
                        return length+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word,length+1))

    return 0

print(solution("hit","cog",["hot","dot","dog","lot","log","cog"]))

"""
Simple idea
Word
 ↓
Create wildcard patterns
 ↓
Find all words with the same pattern
 ↓
Those words differ by one character
 ↓
Use BFS to find the shortest path
The key concept is:
all_combo_dict helps you find neighbouring words quickly, and BFS guarantees that the first time you reach endWord, you have found the shortest transformation sequence.
"""