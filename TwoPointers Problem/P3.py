"""
Problem Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples
Example 1:
(Note: Imagine a bar chart where the area is determined by the shorter of two bars multiplied by the distance between them.)
Input:

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output:
49

"""

def ContainerWithMostWater(h1):
    
    i=0
    j=len(h1)-1
    result=0
    while i<j:
        height = min(h1[i],h1[j])
        result = max(height*(j-i),result)
        if h1[i]<h1[j]:
            i+=1
        else:
            j-=1

    return result

        
print(ContainerWithMostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))

