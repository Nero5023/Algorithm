# -*- coding:utf-8 -*-

class LongestString:
    def getLongest(self, s, n):
        # write code here
        strArr = s
        strArr.sort(key=len)
        strSet = set()
        strSet.add(strArr[0])
        maxLength = 0
        for string in strArr[1:]:
            if checkIfContainSub(string, strSet):
                maxLength = len(string)
            strSet.add(string)
            # print strSet
        return maxLength

def checkIfContainSub(string, strSet):
    if string == "":
        return True
    for i in range(1, len(string)+1):
        subStr = string[:i]
        if subStr in strSet:
            res = checkIfContainSub(string[i:], strSet)
            if res == True:
                return True
    return False

if __name__ == '__main__':
    print LongestString().getLongest(["a","b","c","ab","bc","abc"],6)