# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Successor:
    def findSucc(self, root, p):
        # write code here
        if root.right is not None:
            return minNode(p)
        else:
            n = root
            while n.parent is not None and n.parent.left != n:
                n = n.parent
            return n.parent
    

def minNode(root):
    if root.left is None:
        return root
    return minNode(root.left)