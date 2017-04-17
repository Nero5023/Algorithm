# -*- coding:utf-8 -*-
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque



class Path:
    # a b is UndirectedGraphNode
    # node's label is None mean have visited
    # def checkPathOrder(self, a, b):
    #     # write code here
    #     if (a == b):
    #         return True
    #     q = deque()
    #     q.append(a)
    #     a.label = None
    #     while len(q) != 0:
    #         vNode = q.popleft()
    #         vNode.label = None
    #         for node in vNode.neighbors:
    #             if node.label is not None:
    #                 if node == b:
    #                     return True
    #                 else:
    #                     q.append(node)
    #     return False

    def checkPathOrder(self, a, b):
        # write code here
        dic = {}
        if (a == b):
            return True
        q = deque()
        q.append(a)
        while len(q) != 0:
            vNode = q.popleft()
            # vNode.label = None
            dic[vNode] = True
            for node in vNode.neighbors:
                if dic.get(node) is None or dic.get(node) == False:
                # and dic.get(node) != False:
                    if node == b:
                        return True
                    else:
                        dic[node] = False
                        q.append(node)
        return False

    def checkPath(self, a, b):
        res = self.checkPathOrder(a,b)
        if res == True:
            return True
        return self.checkPathOrder(b,a)


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

if __name__ == '__main__':
    a = UndirectedGraphNode(1)
    b = UndirectedGraphNode(2)
    c = UndirectedGraphNode(3)
    d = UndirectedGraphNode(4)
    e = UndirectedGraphNode(5)
    f = UndirectedGraphNode(6)
    g = UndirectedGraphNode(7)
    h = UndirectedGraphNode(8)
    i = UndirectedGraphNode(9)
    a.neighbors = [b,c,d,f,g]
    b.neighbors = [b, f, g, h]
    c.neighbors = [i]
    p = Path()
    print p.checkPath(i,a)