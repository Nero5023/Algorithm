from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        if len(dic1) > len(dic2):
            temp = dic1
            dic1 = dic2
            dic2 = temp
        res = []
        for key in dic1:
            dic2Res = dic2.get(key, 0)
            num = min(dic2Res, dic1[key])
            for _ in range(num):
                res.append(key)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.intersect([1, 2, 2, 1], [2, 2])