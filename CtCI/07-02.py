# -*- coding:utf-8 -*-
from math import pow
class Ants:
    def antsCollision(self, n):
        # write code here
        p = 1.0/2
        return 1-2*pow(p,n)

if __name__ == '__main__':
    a = Ants()
    print a.antsCollision(3)