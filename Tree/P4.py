"""
Problem Description
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:

A binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Examples
Example 1
Input:
root = [3, 9, 20, null, null, 15, 7]
Output:
true
Example 2
Input:
root = [1, 2, 2, 3, 3, null, null, 4, 4]
Output:
false
Explanation:
The subtree rooted at 2 (the left child of the root) has a left subtree height of 2 and a right subtree height of 0. The difference is:
2 > 1
Therefore, the tree is not height-balanced.

"""

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.item = value
        self.left = left
        self.right = right

def buildTree(l1):
    if not l1:
      return None
    
    root = Node(l1[0])
    i=1
    queue = [root]
    while(i<len(l1)):
        current = queue.pop(0)
        if l1[i] is not None:
            current.left = Node(l1[i])
            queue.append(current.left)
        i+=1
        if l1[i] is not None:
            current.right = Node(l1[i])
            queue.append(current.right)
        i+=1
        
    return root

def isBalanced(root):
    if not root:
        return 0
   
    def getHeight(head):
        if not head:
            return 0
        left_height = getHeight(head.left)
        if left_height == -1:
            return -1
        right_height = getHeight(head.right)
        if right_height == -1:
            return -1
        if abs(left_height-right_height) > 1:
            return -1

        return  max(left_height,right_height)+1 
    
    return getHeight(root)!=-1
    

nodes = [3, 9, 20, None, None, 15, 7]

root = buildTree(nodes)
print(isBalanced(root))
# [1, 2, 2, 3, 3, null, null, 4, 4]
# [3, 9, 20, None, None, 15, 7]