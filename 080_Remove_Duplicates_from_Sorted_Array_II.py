class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        lastNum = None
        apperTiwce = False
        for x in nums:
            if lastNum is None or lastNum != x:
                nums[res] = x
                res += 1
                lastNum = x
                apperTiwce = False
            else:
                if apperTiwce == False:
                    nums[res] = x
                    res += 1
                    apperTiwce = True
        print nums[:res]
        return res

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,1,2,2,3])