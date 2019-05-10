# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:55:01 2018

@author: DinoBob
"""
# Construct a node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
        
def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val)
        printinorder(root.right)
        
        
        
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    
    if p and q:
        if p.val == q.val:
            isSameTree(p.left, q.left)
            isSameTree(p.right, q.right)
        else:
            return False
    elif not p and not q:
        pass
    else:
        return False
    

def lrswap(root):
    if root.left and root.right:
        root.left, root.right = lrswap(root.right), lrswap(root.left)
    elif root.left:
        root.right = lrswap(root.left)
        root.left = None
    elif root.right:
        root.left = lrswap(root.right)
        root.right = None
    return root  

        
        
        
def height(root):
    if root:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
    else:
        return 0
    
def inorderTraversal(root):
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        if isinstance(node, int):
            ans.append(node)
        else:
            if node.right:
                stack.append(node.right)
            stack.append(node.val)
            if node.left:
                stack.append(node.left)
    return ans
        
        
# Insert new nodes
        
def insert(root, node):
    if root == None:
        root = node
    else:
        if root.val > node.val:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
                
test = Node(2)
test.right = Node(3)
test.right.right = Node(5)
test.left = Node(1)
test.left.left = Node(0)
inorderTraversal(test)


#print(isSameTree(test, test))