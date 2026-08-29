"""
Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit
the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules:

1. You only have two baskets, and each basket can only hold a single type of fruit.
2. Starting from any tree, you must pick exactly one fruit from every tree while moving
   to the right. Stop when you encounter a fruit type that cannot fit in your baskets.

Return the maximum total number of fruits you can collect.
"""

def maxFruit(l1):
    l2=[]
    start=0
    result=0
    window=0
    for end in range(len(l1)):
        window+=1
        if l1[end] in l2 or len(l2)<2:
            result=max(window,result)
            l2.append(l1[end])
        else:
            window-=1
            l2.pop(0)
            l2.append(l1[end])
            start+=1
    return result

print(maxFruit([1,2,3,2,2]))

# =================  Standard way to solve the Problem  ======================= 

def solution(fruits):
    max_length=0
    left=0
    count={}

    for right in range(len(fruits)):
        fruit=fruits[right]
        count[fruit]=count.get(fruit,0)+1

        while len(count)>2:
            left_fruit=fruits[left]
            count[left_fruit] -=1

            if count[left_fruit]==0:
                del count[left_fruit]
            left +=1

        max_length=max(max_length,right-left+1)
    return max_length

print(solution([0, 1, 2, 2]))




            

