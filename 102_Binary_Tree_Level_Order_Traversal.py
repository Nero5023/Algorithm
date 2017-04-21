# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque()
        newQueue = deque()
        queue.append(root)
        res = []
        rowRes = []
        while len(queue) != 0:
            node = queue.popleft()
            rowRes.append(node.val)
            if node.left is not None:
                newQueue.append(node.left)
            if node.right is not None:
                newQueue.append(node.right)
            if len(queue) == 0:
                res.append(rowRes)
                rowRes = []
                queue = newQueue
                newQueue = deque()

        if len(rowRes) != 0:
            res.append(rowRes)
        return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node2.left = node3
    node3.left = node4
    node4.left = node5
    print Solution().levelOrder(node1)