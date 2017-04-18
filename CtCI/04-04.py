# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeLevel:
    def __init__(self):
        self.linkedList = None

    def getTreeLevel(self, root, dep):
        # write code here
        self.linkedList = None
        self.traverse(root, 1, dep)
        return self.linkedList

    def traverse(self, node, depth, targetDepth):
        if node is None:
            return
        if depth == targetDepth:
            if self.linkedList is None:
                self.linkedList = ListNode(node.val)
                return
            else:
                newLinkNode = ListNode(node.val)
                newLinkNode.next = self.linkedList
                self.linkedList = newLinkNode
                return
        self.traverse(node.right, depth+1, targetDepth)
        self.traverse(node.left, depth+1, targetDepth)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
if __name__ == '__main__':
    tree = TreeNode(0)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    t = TreeLevel()
    res = t.getTreeLevel(tree, 2)
    while res is not None:
        print res.val
        res = res.next
