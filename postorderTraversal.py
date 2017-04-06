# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversalRe(root, res)
        return res
        

    def postorderTraversalRe(self, root, res):
        if root is None:
            return
        self.postorderTraversalRe(root.left, res)
        self.postorderTraversalRe(root.right, res)
        res.append(root.val)