# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        inOrder(root, output)
        for i in range(0, len(output)-1):
            if output[i] > output[i+1]:
                return False
        return True

def inOrder(root, output):
    if root is None:
        return
    inOrder(root.left, output)
    output.append(root.val)
    inOrder(root.right, output)
