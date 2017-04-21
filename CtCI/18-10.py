# -*- coding:utf-8 -*-
from collections import defaultdict
from collections import deque
class Change:
    def countChanges(self, dic, n, s, t):
        # write code here
        newDic = createNewDic(dic, len(s))
        return len(self.bfsSearch(newDic, s, t))-1

    def bfsSearch(self, dic, source, target):
        queue = deque()
        queue.append(source)
        visitedSet = set()
        visitedSet.add(source)
        backMap = {}
        while len(queue) != 0:
            strNow = queue.popleft()
            oneEditedStrs = getOneEditedWord(strNow, dic, visitedSet)
            for oneEditS in oneEditedStrs:
                if oneEditS == target:
                    backMap[oneEditS] = strNow
                    path = getPath(backMap, target)
                    return path
                queue.append(oneEditS)
                visitedSet.add(oneEditS)
                backMap[oneEditS] = strNow
        return False

def getOneEditedWord(s, dic, visitedSet):
    res = []
    for i in range(0, len(s)):
        reStr = s[:i] + "*" + s[i+1:]
        matchStrs = dic[reStr]
        for matchStr in matchStrs:
            if matchStr == s or matchStr in visitedSet:
                continue
            res.append(matchStr)
    return res

def getPath(backMap, target):
    if target is None:
        return []
    paths = getPath(backMap, backMap.get(target))
    paths.append(target)
    return paths

def createNewDic(strArr, strLen):
    dic = defaultdict(list)
    for s in strArr:
        if len(s) == strLen:
            putStrInDic(s, dic)
    return dic

def putStrInDic(s, dic):
    for string in differentStrs(s):
        dic[string].append(s)

def differentStrs(s):
    strList = list(s)
    res = []
    for i in range(0, len(s)):
        cStrList = strList[:]
        cStrList[i] = "*"
        res.append("".join(cStrList))
    return res


if __name__ == '__main__':
    print Change().countChanges(["vvz","bbaa","f","bbba","bbaa","baoa","btoa","bbba","dcki","bbbb","ge","atoj","baaa","btoj","ae"],15,"atoj","bbbb")