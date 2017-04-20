# -*- coding:utf-8 -*-

class UnusualAdd:
    def addAB(self, A, B):
        # write code here
        if B != 0:
            sumWithOutCarry = A^B
            carry = (A&B) << 1
            return self.addAB(sumWithOutCarry, carry)
        return A
