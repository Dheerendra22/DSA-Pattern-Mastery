"""
Problem Description
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

The length of a path is represented by the number of edges between the two nodes.

Example 1
Input:
root = [1, 2, 3, 4, 5]
Output:
3
Explanation:
The longest path can be:
4 → 2 → 1 → 3
or
5 → 2 → 1 → 3
Both paths contain 3 edges, so the diameter is 3.
Example 2
Input:
root = [1, 2]
Output:
1

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

def findDiameter(root):
    if not root:
        return 0
    Dia = 0
    def getHeight(head):
        nonlocal Dia
        if not head:
            return 0
        left_height = getHeight(head.left)
        right_height = getHeight(head.right)
        Dia = max(Dia,(left_height+right_height))

        return max(left_height,right_height)+1
    getHeight(root)
    return Dia

nodes = [1, 2, 3, 4, 5]

root = buildTree(nodes)
print(findDiameter(root))