"""
Problem Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).

Examples
Example 1
Input:
root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
Output:
3
Explanation:
The LCA of nodes 5 and 1 is 3.
Example 2
Input:
root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
Output:
5
Explanation:
The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

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

def lca(root,p,q):
    if not root or root.item==p or root.item==q:
        return root 
    left=lca(root.left,p,q)
    right=lca(root.right,p,q)

    if left and right:
        return root 
    return left if left else right 

nodes =  [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
root = buildTree(nodes)
result=lca(root,p,q)
print(result.item)
