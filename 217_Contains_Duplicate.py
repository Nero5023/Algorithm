from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = Counter(nums)
        for key in dic:
            if dic[key] > 1:
                return True
        return False