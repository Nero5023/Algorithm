# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.iter(root)
        return self.res

    def iter(self, tree):
        if tree is None:
            return
        self.iter(tree.left)
        # res.append(tree.val)
        self.res.append(tree.val)
        self.iter(tree.right)

    def inorderTraversalWithStack(self, root):
        res, stack = [], []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right