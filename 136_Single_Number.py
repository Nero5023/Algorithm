from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequence = defaultdict(int)
        for num in nums:
            frequence[num] += 1
        for key in frequence:
            if frequence[key] == 1:
                return key
            