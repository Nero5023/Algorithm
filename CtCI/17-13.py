# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minNode(node):
    if node.left is None:
        return node
    # node.left is not None
    return minNode(node.left)

def maxNode(node):
    if node.right is None:
        return node
    return maxNode(node.right)



class Converter:
    def treeToList(self, root):
        # write code here
        treeNode = self.compressTree(root)[0]
        return self.copy(treeNode)

    def compressTree(self, root):
        if root.left is None and root.right is None:
            return (root, root)
        if root.left is None:
            (rightMin, _) = self.compressTree(root.right)
            root.right = rightMin
            rightMin.left = root
            return (root, maxNode(rightMin))
        if root.right is None:
            (_, leftMax) = self.compressTree(root.left)
            leftMax.right = root
            root.left = leftMax
            return (minNode(leftMax),root)

        (_, leftMax) = self.compressTree(root.left)
        (rightMin, _) = self.compressTree(root.right)
        # rightMin = minNode(root.right)
        # leftMax  = maxNode(root.left)
        leftMax.right = root
        root.left = leftMax
        root.right = rightMin
        rightMin.left = root
        return (minNode(root), maxNode(root))

    def copy(self, treeNode):
        list = ListNode(treeNode.val)
        iter = list
        treeNode = treeNode.right
        while treeNode is not None:
            newListNode = ListNode(treeNode.val)
            iter.next = newListNode
            iter = iter.next
            treeNode = treeNode.right
        return  list

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5
    node4.left = node6
    x = Converter().treeToList(node1)
    # list = x
    while x is not None:
        print x.val
        x = x.next

