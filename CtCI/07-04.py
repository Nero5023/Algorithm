# -*- coding:utf-8 -*-
class AddSubstitution:
    def calc(self, a, b, t):
        # write code here
        if (t == 1):
            return mul(a, b)
        if (t == 0):
            return div(a, b)
        if (t == -1):
            return  sub(a, b)
    
def negative(a):
    delta = 1
    if a > 0:
        delta = -1
    res = 0
    while a != 0:
        a += delta
        res += delta
    return res

def myAbs(a):
    if a < 0:
        return negative(a)
    return a
    
def sub(a,b):
    return a + negative(b)

def mul(a,b):
    needNeg = False
    if b < 0:
        b = negative(b)
        needNeg = True
    res = 0
    for _ in range(0,b):
        res += a
    if needNeg:
        res = negative(res)
    return res

def div(a,b):
    needNeg = False
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        needNeg = True
    if b == 0:
        raise ZeroDivisionError()
    a = myAbs(a)
    b = myAbs(b)
    if a < b:
        return 0
    i = 0
    cal = b
    while a >= cal:
        i += 1
        cal += b
    if needNeg:
        i = negative(i)
    return i

if __name__ == '__main__':
    print mul(-1, -10)
    print div(10, -2)


