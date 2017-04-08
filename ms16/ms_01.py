from math import sqrt
def maxFointSize(parCount, maxPage, width, heidht, parsChars):
    def linesInPars(size):
        numOfChaOneLine = width//size
        return map(calculateLine(numOfChaOneLine), parsChars)

    def toPages(lines, size):
        line = sum(lines)
        numOfLineOnePage = heidht//size
        if line % numOfLineOnePage == 0:
            return line//numOfLineOnePage
        else:
            return line//numOfLineOnePage + 1


    totoalChars = sum(parsChars)
    size = sqrt(maxPage*width*heidht*1.0/(totoalChars*1.0))
    size = int(size)
    while True:
        lines = linesInPars(size)
        p = toPages(lines, size)
        if p <= maxPage:
            return size
        else:
            size-=1




def calculateLine(numOfChaOneLine):
    def inner(chas):
        if chas % numOfChaOneLine == 0:
            return chas//numOfChaOneLine
        else:
            return chas//numOfChaOneLine + 1
    return inner


def catInput():
    numOfCase = raw_input()
    numOfCase = int(numOfCase)
    for _ in range(0, numOfCase):
        (N, P, W, H) = (int(x) for x in raw_input().split())
        pars = [int(x) for x in raw_input().split()]
        print maxFointSize(N,P,W,H,pars)

# if __name__ == '__main__':
#     print(maxFointSize(1, 10, 4, 3, [10]))
#     print(maxFointSize(2, 10, 4, 3, [10, 10]))
#     catInput()


while True:
    try:
        catInput()
    except EOFError:
        break