import copy

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return 1

    def countArrangementIter(self, n):
        if n == 1:
            return [[1]]
        # n >= 2
        nm1Arranges = self.countArrangementIter(n-1)
        newArranges = map(lambda xs:xs + [n], nm1Arranges)
        res = copy.deepcopy(newArranges)
        for arrgument in newArranges:
            for i in range(0, n-1):
                arrC = exchange(arrgument, i, n-1)
                if checkIfSatisty(arrC, i) and checkIfSatisty(arrC, n-1):
                    res.append(arrC)
        return res


def exchange(arr, i, j):
    arrC = arr[:]
    temp = arrC[i]
    arrC[i] = arrC[j]
    arrC[j] = temp
    return arrC

def checkIfSatisty(arr, i):
    value = arr[i]
    index = i + 1
    if value % index == 0 or index % value == 0:
        return True
    return False

if __name__ == '__main__':
    print Solution().countArrangementIter(6)