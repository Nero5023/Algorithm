
def queueIter(n):
    if n == 0:
        return [[]]
    lastPairs = queueIter(n-1)
    res = []
    for x in range(1,9):
        for pair in lastPairs:
            pair = pair[:]
            if safe(x, pair, 0):
                pair.append(x)
                res.append(pair)

    return res

def safe(x, pair, level):
    if level >= len(pair):
        return True
    y = pair[level]
    if x == y:
        return False
    xLevel = len(pair)
    diffLevel = xLevel - level
    if x == y + diffLevel or x == y - diffLevel:
        return False
    return safe(x, pair, level+1)


if __name__ == '__main__':
    print queueIter(8)