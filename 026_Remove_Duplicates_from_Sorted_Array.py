class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        lastNum = None
        for x in nums:
            if lastNum is None or lastNum != x:
                nums[res] = x
                res += 1
                lastNum = x
        return res

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,2])