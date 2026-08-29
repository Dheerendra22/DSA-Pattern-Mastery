"""
Problem Description
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples
Example 1
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3

Example 2
Input: root = [1, null, 2]
Output: 2

Constraints
The number of nodes in the tree is in the range [0, 10⁴].

"""

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.item = value
        self.left = left
        self.right = right

def maxDepth(root):
    if not root :
        return 0
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return max(left_height,right_height)+1

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
 
nodes = [3, 9, 20, None, None, 15, 7]
root = buildTree(nodes)
print(maxDepth(root))

    
        
        