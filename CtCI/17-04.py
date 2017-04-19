# -*- coding:utf-8 -*-


def flip(x):
    return x^1

def sign(x):
    return flip(x >> 31 & 0x01)

# max = k*a + q*b
class Max:
    def getMax(self, a, b):
        # write code here
        signA = sign(a)
        signB = sign(b)

        signForSinA = signA ^ signB
        signForSinA_B = flip(signForSinA)

        k = signForSinA*signA + signForSinA_B*sign(a-b)

        q = flip(k)
        return k*a + q*b

if __name__ == '__main__':
    print sign(-10)
    print Max().getMax(10,1)