from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        upperBound = 0
        res = -1
        for index, num in enumerate(self.nums):
            if num == target:
                if randint(0, upperBound) == 0:
                    res = index
                upperBound+=1
        return res

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)