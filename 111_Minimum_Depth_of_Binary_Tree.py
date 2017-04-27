# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        backTrackMap = {}
        queue = deque()
        queue.append(root)
        firstLeaf = None
        while len(queue) != 0:
            node = queue.popleft()
            if node is None:
                continue
            if node.left is None and node.right is None:
                firstLeaf = node
                break
            queue.append(node.left)
            queue.append(node.right)
            backTrackMap[node.left] = node
            backTrackMap[node.right] = node
        count = 0
        while firstLeaf is not None:
            count += 1
            firstLeaf = backTrackMap.get(firstLeaf)
        return count


# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         return minHeight(root)

# def minHeight(root):
#     if root is None:
#         return 0
#     left = minHeight(root.left)
#     right = minHeight(root.right)
#     if left == 0 or right == 0:
#         return left + right + 1
#     return min(left, right) + 1