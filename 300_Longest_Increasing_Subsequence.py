class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            low, high = 0, size
            while low != high:
                mid = (low + high)/2
                if tails[mid] < x:
                    low = mid+1
                else:
                    high = mid
            tails[low] = x
            size = max(low+1, size)
        return size


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLIS([2,2])