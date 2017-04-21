# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return dfsHeight(root) != -1

def dfsHeight(root):
    if root is None:
        return 0
    leftDFSHeight = dfsHeight(root.left)
    if leftDFSHeight == -1:
        return -1
    rightDFSHeight = dfsHeight(root.right)
    if rightDFSHeight == -1:
        return -1
    if abs(rightDFSHeight - leftDFSHeight) > 1:
        return -1
    return 1 + max(rightDFSHeight, leftDFSHeight)



# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# cache = {}
# class Solution(object):
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True
#         leftIsBalance = self.isBalanced(root.left)
#         if leftIsBalance == False:
#             return False
#         rightIsBalance = self.isBalanced(root.right)
#         if rightIsBalance == False:
#             return False
#         if abs(heightOfTree(root.left, cache)-heightOfTree(root.right, cache)) > 1:
#             return False
#         return True

# def heightOfTree(root, cache):
#     if root in cache:
#         return root[cache]
#     if root is None:
#         return 0
#     return 1 + max(heightOfTree(root.left, cache), heightOfTree(root.right, cache))