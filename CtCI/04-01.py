# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Balance:
    def isBalance(self, root):
        # write code here
        (_, isB) = self.isBalanceIter(root)
        return isB

    # (height, isBalance)
    def isBalanceIter(self, node):
        if node is None:
            return (0, True)
        (leftH, leftB) = self.isBalanceIter(node.left)
        if not leftB:
            return (leftH, False)
        (rightH, rightB) = self.isBalanceIter(node.right)
        if not rightB:
            return (rightH, False)
        if abs(leftH - rightH) <= 1:
            return (max(leftH, rightH)+1, True)
        else:
            return (max(leftH, rightH)+1, False)

