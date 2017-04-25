# -*- coding:utf-8 -*-

class Middle:
    def __init__(self):
        self.tree = None

    def getMiddle(self, A, n):
        # write code here
        res = []
        for val in A:
            midVal = self.getMiddleIter(val)
            res.append(midVal)
        return res


    def getMiddleIter(self, x):
        self.tree = insert(self.tree, x)
        if sizeOfTree(self.tree.left) == sizeOfTree(self.tree.right):
            return self.tree.val
        if sizeOfTree(self.tree.left) + 1 == sizeOfTree(self.tree.right):
            return self.tree.val
        if sizeOfTree(self.tree.left) == sizeOfTree(self.tree.right) + 1:
            leftMaxNode = maxNode(self.tree.left)
            return leftMaxNode.val
        # sizeOfTree(tree.left) - sizeOfTree(tree.right) abs > 1
        # if sizeOfTree(tree.left) > sizeOfTree(tree.right):
        self.tree = babanceTree(self.tree)
        return self.tree.val



class TreeNode():
    """docstring for TreeNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1


def sizeOfTree(root):
    if root is None:
        return 0
    else:
        return root.size

def insert(root, x):
    if root is None:
        return TreeNode(x)
    if x <= root.val:
        root.left = insert(root.left, x)
    if x > root.val:
        root.right = insert(root.right, x)
    root.size = sizeOfTree(root.left) + sizeOfTree(root.right) + 1
    return root

def maxNode(root):
    if root.right is None:
        return root
    return maxNode(root.right)

def minNode(root):
    if root.left is None:
        return root
    return minNode(root.left)

def delMax(root):
    # maxNodeToDel = maxNode(root)
    tree = None
    if root.right is None:
        tree = root.left
    else:
        root.right = delMax(root.right)
        tree = root
    if tree is None:
        return tree
    tree.size = sizeOfTree(tree.left) + sizeOfTree(tree.right) + 1
    return tree

def delMin(root):
    # maxNodeToDel = maxNode(root)
    tree = None
    if root.left is None:
        tree = root.right
    else:
        root.left = delMin(root.left)
        tree = root
    if tree is None:
        return tree
    tree.size = sizeOfTree(tree.left) + sizeOfTree(tree.right) + 1
    return tree

# 2 level diff
def babanceTree(tree):
    if sizeOfTree(tree.left) < sizeOfTree(tree.right):
        treeVal = tree.val
        rightMinVal = minNode(tree.right).val
        tree.val = rightMinVal
        tree.left = insert(tree.left, treeVal)
        tree.right = delMin(tree.right)
        tree.size = sizeOfTree(tree.left) + sizeOfTree(tree.right) + 1
        return tree
    else:
        treeVal = tree.val
        leftMaxVal = maxNode(tree.left).val
        tree.val = leftMaxVal
        tree.right = insert(tree.right, treeVal)
        tree.left = delMax(tree.left)
        tree.size = sizeOfTree(tree.left) + sizeOfTree(tree.right) + 1
        return tree


if __name__ == '__main__':
    print Middle().getMiddle([236312,116289,257841,40359,21993,121674,68768,288444,98015,118071,130963,221777,71589,233048,89053,20048,264772,141943,170253,299901,193849,211453,198250,280383,126656,4775,229057,119532],6)
