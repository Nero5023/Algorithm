class Queue():
    def __init__(self, initvalues = []):
        self.leftStack = initvalues[::-1]
        self.rightStack = []

    def enque(self, value):
        self.rightStack.append(value)

    def deque(self):
        if len(self.leftStack) + len(self.rightStack) == 0:
            raise Exception("queue is Empty")
        if len(self.leftStack) == 0:
            self.leftStack = self.rightStack[::-1]
            self.rightStack = []

        return self.leftStack.pop()
        

if __name__ == '__main__':
    q = Queue()
    q.enque(4)
    q.enque(3)
    q.enque(2)
    q.enque(1)
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())