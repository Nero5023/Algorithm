# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return height(root)
        
def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1+max(left, right)