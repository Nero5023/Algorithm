# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        height = maxDepth(root)
        paths = [0]*(height+1)
        res = []
        self.findPathIter(root, expectNumber, 1, paths, res)
        return res


    # paths is from 
    def findPathIter(self, root, expectNumber, level, paths, res):
        if root is None:
            return
        paths[level] = root.val
        innerSum = 0
        for i in range(level, 0, -1):
            innerSum += paths[i]
            if innerSum == expectNumber:
                validPath = printPaths(paths, i, level)
                res.append(validPath)
        self.findPathIter(root.left, expectNumber, level+1, paths, res)
        self.findPathIter(root.right, expectNumber, level+1, paths, res)


def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def printPaths(paths, start, end):
    res = []
    for i in range(start, end+1):
        sys.stdout.write(str(paths[i]))
        res.append(paths[i])
        if i != end:
            sys.stdout.write(" -> ")
    print ""
    return res


class TreeNode:
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
    print Solution().FindPath(node1, 3)