import heapq
import copy

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item):
        heapq.heappush(self._queue, (item.priority(), self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def min(self):
        # print type(self._queue[0])
        # print self._queue[0][2]
        return self._queue[0][2]


class Board:
    def __init__(self, blocks, average):
        self.bolcks = blocks
        self.average = average

    def diff(self):
        dif = 0
        for xs in self.bolcks:
            for x in xs:
                dif += abs(x - self.average)
        return dif

    def isGoal(self):
        return self.diff()==0

    def findMaxIndex(self):
        max = 0
        tI = 0
        tJ = 0
        for i in range(0,2):
            for j in range(0, len(self.bolcks[0])):
               if self.bolcks[i][j] > max:
                    max = self.bolcks[i][j]
                    tI = i
                    tJ = j
        return (tI, tJ)


    def neighbour(self):
        (tI, tJ) = self.findMaxIndex()
        moves = []
        for (offx, offy) in [(-1,0), (1,0), (0, 1), (0, -1)]:
            x = tI + offx
            y = tJ + offy
            if y >= len(self.bolcks[0]) or y < 0:
                continue
            if x >= 2 or x < 0:
                continue
            moves.append((x,y))

        res = []
        for move in moves:
            copyArr = copy.deepcopy(self.bolcks)
            moveFromto(copyArr, (tI, tJ), move)
            res.append(Board(copyArr, self.average))
        return res

    def isSame(self, board):
        for i in range(0, 2):
            for j in range(0, len(self.bolcks[0])):
                if self.bolcks[i][j] != board[i][j]:
                    return False
        return True



def moveFromto(array, fromP, toP):
    (x0, y0) = fromP
    (x1, y1) = toP
    array[x0][y0] -= 1
    array[x1][y1] += 1

class SearchNode:
    def __init__(self, board, move, previous):
        self.board = board
        self.move = move
        self.previous = previous

    def __cmp__(self, anOther):
        diff0 = self.board.diff() + self.move
        diff1 = anOther.board.diff() + anOther.move
        cmp = diff0 - diff1
        if (cmp < 0):
            return -1
        elif cmp == 0:
            return 0
        else:
            return 1

    def priority(self):
        return self.board.diff() + self.move



if __name__ == "__main__":

    blocks = [[3,4, 5], [6,7,5]]
    totoalSum = sum(map(sum, blocks))
    average = totoalSum / (len(blocks[0]) * 2)

    initial = Board(blocks, average)
    sn = SearchNode(initial, 0 , None)
    pq = PriorityQueue()
    pq.push(sn)
    while not pq.min().board.isGoal():
        sn = pq.pop()
        for neb in sn.board.neighbour():
            pq.push(SearchNode(neb, sn.move+1, sn))
    sn = pq.pop()
    print sn.move

