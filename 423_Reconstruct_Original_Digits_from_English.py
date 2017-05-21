from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        info = Counter(s)
        res = ""
        # # 0
        # for _ in range(info.get('z', 0)):
        #     res.append('0')
        #     updateInfoDic('zero')
        # # 2
        # for _ in range(info.get('w', 0)):
        #     res.append('')
        res = findNum('zero', 'z', 0, info, res)
        res = findNum('two', 'w', 2, info, res)
        res = findNum('four', 'u', 4, info, res)
        res = findNum('six', 'x', 6, info, res)
        res = findNum('eight', 'g', 8, info, res)
        res = findNum('one', 'o', 1, info, res)
        res = findNum('three', 'h', 3, info, res)
        res = findNum('five', 'f', 5, info, res)
        res = findNum('seven', 's', 7, info, res)
        res = findNum('nine', 'i', 9, info, res)
        res = list(res)
        res.sort()
        return ''.join(res)


def updateInfoDic(numstr, info):
    for x in numstr:
        info[x] -= 1

def findNum(numstr, keyWord,digit, info, lastStr):
    for _ in range(info.get(keyWord, 0)):
        lastStr+=(str(digit))
        updateInfoDic(numstr, info)
    return lastStr

if __name__ == '__main__':
    s = Solution()
    print s.originalDigits("owoztneoer")