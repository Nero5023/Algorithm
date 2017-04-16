class Node(object):
    """docstring for Node"""
    def __init__(self, val):
        super(Node, self).__init__()
        self.val = val
        self.next = None

    def iterable(self):
        node = self
        while node is not None:
            yield node
            node = node.next

def linkedListLaskKthNode(k, node):
    length = 0
    for _ in node.iterable():
        length += 1
    if k > length:
        return None
    i = length + 1 - k 
    j = 0
    for x in node.iterable():
        j+=1
        if i == j:
            return x


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    for n in node1.iterable():
        print n.val

    x = linkedListLaskKthNode(2, node1)
    print x.val