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
    list1 = Node(0)
    list1c = list1
    list2 = Node(0)
    list2c = list2
    for n in node1.iterable():
        # print n.val
        if n.val <= 3:
            list1c.next = n
            list1c = list1c.next
        else:
            list2c.next = n
            list2c = list2c.next
    list1c.next = None
    list2c.next = None
    for x in list1.next.iterable():
        print x.val
    print "----"
    for y in list2.next.iterable():
        print y.val
        # if n.next is not None and n.next.val == 2:
        #     n.next = n.next.next
        # print n.val

    # x = linkedListLaskKthNode(2, node1)
    # print x.val