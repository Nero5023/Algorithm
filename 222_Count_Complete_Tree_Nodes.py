# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftDepth  = depthLeft(root)
        rightDepth = depthRight(root)
        if leftDepth == rightDepth:
            return (1 << leftDepth) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

def depthLeft(root):
    if root is None:
        return 0
    else:
        return 1 + depthLeft(root.left)

def depthRight(root):
    if root is None:
        return 0
    else:
        return 1 + depthRight(root.right)