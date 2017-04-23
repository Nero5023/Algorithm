# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Checker:
    def checkBST(self, root):
        # write code here
        return checkBSTIter(root, -sys.maxint, sys.maxint)


def checkBSTIter(root, minVal, maxVal):
    if root is None:
        return True
    if root.val > maxVal or root.val < minVal:
        return False
    return checkBSTIter(root.left, minVal, root.val) and checkBSTIter(root.right, root.val+1, maxVal)