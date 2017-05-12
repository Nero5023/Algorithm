class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        conbimed = zip(*map('{:032b}'.format, nums))
        res = reduce(lambda res, x: res + x.count('0')*x.count('1'), conbimed, 0)
        return res




def hammingDistance(a,b):
    dis = 0
    val = a^b
    while val != 0:
        dis+=1
        val = (val - 1) & val
    return dis

if __name__ == '__main__':
    s = Solution()
    print s.totalHammingDistance([4,14,2])