# -*- coding:utf-8 -*-
class LCA:
    # method1
    # def getLCA(self, root, nodeA, nodeB):
    #     # write code here
    #     if root is None:
    #         return None
    #     leftRes = self.getLCA(root.left, nodeA, nodeB)
    #     rightRes = self.getLCA(root.left, nodeA, nodeB)
    #     if leftRes is not None:
    #         return leftRes
    #     if rightRes is not None:
    #         return rightRes
    #     nodeAExist = contains(root, nodeA)
    #     nodeBExist = contains(root, nodeB)
    #     if !nodeAExist or !nodeBExist:
    #         return None
    #     return root

    # method2
    def getLCA2Iter(self, root, nodeA, nodeB):
        if root is None:
            return None
        if root == nodeA or root == nodeB:
            return root
        aIsOnLeft = contains(root.left, nodeA)
        bIsOnLeft = contains(root.left, nodeB)
        if aIsOnLeft != bIsOnLeft:
            return root
        if aIsOnLeft:
            return getLCA2Iter(root.left, nodeA, nodeB)
        else:
            return getLCA2Iter(root.right, nodeA, nodeB)

    def getLCA2(self, root, nodeA, nodeB):
        if !contains(root, nodeA) or !contains(root, nodeB):
            return None
        return self.getLCA2Iter(root, nodeA, nodeB)

    # (node to find, isFindResult)
    def getLCABest(self, root, nodeA, nodeB):
        if root is None:
            return (None, False)
        if root == nodeA and root == nodeB:
            return (root, True)
        (leftResNode, leftResIs) = self.getLCABest(root.left, nodeA, nodeB)
        if leftResIs == True:
            return (leftResNode, leftResIs)
        (rightResNode, rightResIs) = self.getLCABest(root.right, nodeA, nodeB)
        if rightResIs == True:
            return (rightResNode, leftResIs)

        if leftResNode is not None and rightResNode is not None:
            return (root, True)
        # leftResIs = leftResIs = false
        # leftResNode is None or rightResNode is None
        # leftResNode rightResNode 都是 None, 或者 一个是 None
        if root == nodeA or root == nodeB:
            if rightResNode is None and leftResNode is None:
                return (root, False)
            else:
                return (root, True)

        # root != nodeA and root != nodeB
        if leftResNode is None:
            return (rightResNode, False)
        else:
            return (leftResNode, False)

            


def contains(root, node):
    if root is None:
        return False
    if root == node:
        return True
    else:
        return contains(root.left, node) or contains(root.right, node)