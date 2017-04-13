from collections import Counter

def main(points):
    xs = map(lambda (x,y):x, points)
    ys = map(lambda (x,y):y, points)
    xmy = map(lambda (x,y): y-x, points)
    xpy = map(lambda (x,y): x+y, points)
    return pairs(Counter(xs)) + pairs(Counter(ys)) + pairs(Counter(xmy)) + pairs(Counter(xpy))

def cn2(n):
    return n*(n-1)/2

def pairs(counterDic):
    res = 0
    for key in counterDic.keys():
        if counterDic[key] != 1:
            res += cn2(counterDic[key])
    return res

if __name__ == '__main__':
    print main([(1,1), (2,2), (3,3), (1,3), (3,1)])