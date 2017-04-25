# -*- coding:utf-8 -*-
from collections import Counter

class Result:
    def calcResult(self, A, guess):
        # write code here
        target = A
        zippedValue = zip(target, guess)
        correct = filter(lambda (x,y): x==y, zippedValue)
        guessed = len(correct)

        filed = filter(lambda (x,y): x!=y, zippedValue)

        target = map(lambda (x,_):x, filed)
        guess = map(lambda (_, y):y, filed)

        targetDic = Counter(target)
        guessDic = Counter(guess)

        gRes = 0
        for key in targetDic.keys():
            if guessDic.get(key) is None:
                gRes += 0
                continue
            t = targetDic[key]
            g = guessDic[key]
            gRes += min(t,g)

        return [guessed, gRes]

if __name__ == '__main__':
    print Result().calcResult("GBBR","BYRR")