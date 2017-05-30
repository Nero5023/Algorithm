# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val != key:
            left  = self.deleteNode(root.left, key)
            right = self.deleteNode(root.right, key)
            root.left  = left
            root.right = right
            return root
        else:
            if root.right is None:
                root = root.left
                return root
            else:
                (val, right) = self.findMinAndDelIt(root.right)
                root.right = right
                root.val = val
                return root

    def findMinAndDelIt(self, root):
        if root.left is None:
            val = root.val
            root = root.right
            return (val, root)
        else:
            (val, left) = self.findMinAndDelIt(root.left)
            root.left = left
            return (val, root)