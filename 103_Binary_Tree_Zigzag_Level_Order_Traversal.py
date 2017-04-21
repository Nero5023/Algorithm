# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        needReverse = False
        while len(queue) != 0:
            node = queue.popleft()
            rowRes.append(node.val)

            if node.left is not None:
                newQueue.append(node.left)
            if node.right is not None:
                newQueue.append(node.right)

            if len(queue) == 0:
                if needReverse:
                    rowRes.reverse()
                needReverse = not needReverse
                res.append(rowRes)
                rowRes = []
                # newQueue.reverse()
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
    node1.right = node3
    node2.left = node4
    node3.right = node5
    print Solution().zigzagLevelOrder(node1)