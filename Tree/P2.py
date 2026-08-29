"""
Problem Description
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Examples
Example 1
Input:
root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1],
targetSum = 22
Output:
true
Explanation:
The root-to-leaf path with the target sum is:
5 → 4 → 11 → 2 = 22
Example 2
Input:
root = [1, 2, 3], targetSum = 5
Output:
false
Explanation: There are two root-to-leaf paths:
1 → 2 (sum = 3)
1 → 3 (sum = 4)
There is no root-to-leaf path with sum = 5.

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

def pathSum(root,target):
    if not root:
        return False

    # If it is a leaf node
    if not root.left and not root.right :
        return root.item == target

    return (
        pathSum(root.left, target - root.item)
        or
        pathSum(root.right, target - root.item)
    )


nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
target = 22
root = buildTree(nodes)
print(pathSum(root,target))
