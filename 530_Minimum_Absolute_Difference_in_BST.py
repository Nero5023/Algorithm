# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = []
        traverse(root, values)
        minValue = sys.maxint
        for i in range(0, len(values)-1):
            diff = abs(values[i]-values[i+1])
            minValue = min(diff, minValue)
        return minValue


def traverse(root, res):
    if root is None:
        return
    traverse(root.left, res)
    res.append(root.val)
    traverse(root.right, res)


