# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findTreeInBigTree(self, bigTree, tree):
        # write code here
        if bigTree.val == tree.val:
            if checkIfSame(bigTree, tree):
                return bigTree
        left = self.findTreeInBigTree(bigTree.left, tree)
        right = self.findTreeInBigTree(bigTree.right, tree)
        if left is None and right is None:
            return None
        if left is None:
            return right
        else:
            return left



def checkIfSame(aTree, bTree):
    if aTree is None and bTree is None:
        return True
    # one of aTree and bTree is None
    if aTree is None or bTree is None:
        return False
    if aTree.val != bTree.val:
        return False
    return checkIfSame(aTree.left, bTree.left) and checkIfSame(aTree.right, bTree.right)
