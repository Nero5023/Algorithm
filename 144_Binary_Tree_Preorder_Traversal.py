# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        track = []
        self.preorderTraversalIter(root, track)
        return track
    

    def preorderTraversalIter(self, root, track):
        if root is None:
            return
        track.append(root.val)
        self.preorderTraversalIter(root.left, track)
        self.preorderTraversalIter(root.right, track)
