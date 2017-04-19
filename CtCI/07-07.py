# -*- coding:utf-8 -*-
class KthNumber:
    def findKth(self, k):
        # write code here
        i3 = i5 = i7 = 0
        if k == 1:
            return 3
        if k == 2:
            return 5
        if k == 3:
            return 7
        res = [0] * k
        res[0] = 3
        res[1] = 5
        res[2] = 7
        x3 = 3*3
        x5 = 5*3
        x7 = 7*3
        for index in range(3,k):
            if x3 < x5 and x3 < x7:
                res[index] = x3
                i3+=1
                x3 = 3 * res[i3]
                continue
            if x5 < x3 and x5 < x7:
                res[index] = x5
                i5+=1
                x5 = 5 * res[i5]
                continue
            if x7 < x5 and x7 < x3:
                res[index] = x7
                i7+=1
                x7 = 7 * res[i7]
                continue
            if x3 == x5 and x3 < x7:
                res[index] = x3
                i3+=1
                x3 = 3 * res[i3]
                i5+=1
                x5 = 5 * res[i5]
                continue
            if x3 == x7 and x3 < x5:
                res[index] = x3
                i3+=1
                x3 = 3 * res[i3]
                i7+=1
                x7 = 7 * res[i7]
                continue
            if x5 == x7 and x5 < x3:
                res[index] = x5
                i5+=1
                x5 = 5 * res[i5]
                i7+=1
                x7 = 7 * res[i7]
                continue
            if x3 == x5 and x5 == x7:
                res[index] = x3
                i3+=1
                x3 = 3 * res[i3]
                i5+=1
                x5 = 5 * res[i5]
                i7+=1
                x7 = 7 * res[i7]
                continue
        return res[-1]

if __name__ == '__main__':
    print KthNumber().findKth(11)